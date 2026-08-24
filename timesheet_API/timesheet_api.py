# THE DESIGN -
# 2 resources - workers and shifts
# workers model holds - another field holding the role either a worker or a admin name 
# and workers_id -> assigned by the server and workers_id is also the primary key in workers
# and shifts model primary key is shift_id
# shift model holds - shift_id, workers_id and a shift needs two — clock-in and clock-out, 
# with clock-out starting empty. None in python or NULL in postgres
# The gaurds - it is against the updation of the clock-out, in the PUT route
# PUT /shifts/{shift_id}/clock-out
# the four gaurds: 1. Shift doesn't exist → 404
# 2. Already clocked out → 409
# 3. Not your shift → 403
# 4. Valid → 200, completed shift returned
# and now the whole clock out design -> clock out returns the hours for that shift and 
# a separte aggreagtion route that handles totals across shifts
# now designing the clock-in route: posting an entry which means we are creating a data for the user 
# so POST /shifts 
# Full design: Resources: workers, shifts
# workers — worker_id (primary key), name, role (default "worker", server-assigned, never client-settable)
# shifts — shift_id (primary key), worker_id (foreign key → workers), clock_in, clock_out (starts null)
# POST /shifts — clock in
# 404 worker doesn't exist · 409 already has an open shift · 201 created
# PUT /shifts/{shift_id}/clock-out
# 404 shift doesn't exist · 409 already clocked out · 403 not your shift · 200 updated
# PUT /shifts/{shift_id}/update-entry — admin correction
# 403 if role isn't admin
# GET aggregation route — hours across shifts, computed on demand
# async with guarantees the connection is returned to the pool when the block ends — even if the route raises. 
# Borrow on entry, release on exit. 
# Without it we would have to write the release yourself and leak connections when a route errored.


from fastapi import FastAPI, Request, Depends, HTTPException
from contextlib import asynccontextmanager
import os
from psycopg_pool import AsyncConnectionPool
from dotenv import load_dotenv
from psycopg.rows import dict_row
from pydantic import BaseModel

load_dotenv() # loading the connection
database_conn = os.environ["DATABASE_URL"] # Connection string to postgres

@asynccontextmanager
async def lifespan(app: FastAPI):
    # opening up the connection to postgres
    # kwargs the argument is the dict of settings passed through, row_factory is the setting itself
    app.state.conn_pool = AsyncConnectionPool(database_conn, kwargs={"row_factory": dict_row}) 
    yield
    # shutdown the connection
    await app.state.conn_pool.close()

app = FastAPI(lifespan=lifespan)

class CreateWorkers(BaseModel):
    name: str

class CreateShift(BaseModel):
    worker_id: int

# dependency function : same shape as of the lifespan function but at a smaller scale
async def get_conn(request: Request):
    async with request.app.state.conn_pool.connection() as conn: # as this is a connection not a pool
        yield conn

# the GET route
@app.get("/shifts")
async def read_data(conn= Depends(get_conn)): # depends points out at where the data gets readed from
    async with conn.cursor() as cur: # cursor is what helps us talk with the database 
        await cur.execute("SELECT * FROM shifts") # accessing shifts table using .execute
        rows = await cur.fetchall() # fetching all the shifts data
        return rows # returning rows 

# POST /shifts route with 2 gaurds where Guard 1 fails when it finds nothing (worker missing). 
# Guard 2 fails when it finds something (open shift exists).
@app.post("/shifts")
async def create_data(create_shift: CreateShift, new_con= Depends(get_conn)):
    async with new_con.cursor() as cur:
        await cur.execute("SELECT worker_id FROM workers WHERE worker_id=%s", (create_shift.worker_id,))
        fetch_worker_row = await cur.fetchone()
        if fetch_worker_row is None:
            raise HTTPException(status_code=404, detail="no matching workers found")
        await cur.execute("SELECT worker_id FROM shifts WHERE worker_id=%s AND clock_out IS NULL", (create_shift.worker_id,))
        fetch_shift_row = await cur.fetchone()
        if fetch_shift_row is not None:
            raise HTTPException(status_code=409, detail="dual shift entry")
        await cur.execute("INSERT INTO shifts (worker_id, clock_in) VALUES (%s, now()) RETURNING *", (create_shift.worker_id,))
        shift_data = await cur.fetchone()
        return shift_data


# POST workers route with no gaurds as there is no check for anything just the worker gets created
@app.post("/workers")
async def create_workers(create_workers: CreateWorkers, conn_workers=Depends(get_conn)):
    async with conn_workers.cursor() as cur:
        await cur.execute("INSERT INTO workers (name) VALUES (%s) RETURNING *", (create_workers.name,))
        workers_rows = await cur.fetchone()
        return workers_rows 

# PUT route for shift clock_out with gaurds 
# 404 shift doesn't exist · 409 already clocked out · 403 not your shift · 200 updated
# to merger both the gaurds i needed to select clock_out and filter on shift_id; clock_out starts as null
@app.put("/shifts/{shift_id}/clock_out")
async def update_ClockOut(shift_id: int, conn_ClockOut=Depends(get_conn)):
    async with conn_ClockOut.cursor() as cur:
        await cur.execute("SELECT clock_out FROM shifts WHERE shift_id=%s", (shift_id,))
        clockOut_rows = await cur.fetchone()
        if clockOut_rows is None:
            raise HTTPException(status_code=404, detail="no shift exist")
        if clockOut_rows is not None:
            raise HTTPException(status_code=409, detail="clocked out exist already")
        await cur.execute("UPDATE shifts SET clock_out = now() WHERE shift_id=%s RETURNING *", (shift_id,)) # no insert 
        # as we are updating the table not inserting values
        clockOut_update = await cur.fetchone()
        return clockOut_update

# the aggregation route
# COALESCE is a SQL function that takes a list of values and returns the first one that isn't NULL
# WHAT extract epoch from does is that it extracts the number out of the interval and EPOCH from is what asking to give the
# total as seconds; /3600 is plain division 3600 is an hour so this converts seconds to hour
@app.get("/workers/{worker_id}/hours")
async def agg_hours(worker_id: int, hours_conn=Depends(get_conn)): # borrowing the connection
    async with hours_conn.cursor() as cur: # .cursor() creates a cursor on the connection
        await cur.execute("SELECT worker_id FROM workers WHERE worker_id=%s", (worker_id,)) # check againts no matching worker_id
        hour_rows = await cur.fetchone()
        if hour_rows is None:
            raise HTTPException(status_code=404, detail="no matching workers found")
        await cur.execute("SELECT ROUND(EXTRACT(EPOCH FROM COALESCE(SUM(clock_out - clock_in), INTERVAL '0')) /3600, 2) AS total_hours FROM shifts WHERE worker_id=%s AND clock_out IS NOT NULL", (worker_id,))
        hours = await cur.fetchone()
        return hours 

# aggregation route to see hours weekly and monthly
@app.get("/workers/{worker_id}/breakdown")
async def breakdown(worker_id: int, period: str = "weekly", breakdown_conn=Depends(get_conn)):
    async with breakdown_conn.cursor() as cur:
        await cur.execute("SELECT worker_id FROM workers WHERE worker_id=%s", (worker_id,))
        breakdown_rows = await cur.fetchone()
        if breakdown_rows is None:
            raise HTTPException(status_code=404, detail="no matching workers found")
# deploying a hanrdcoded dict instead of passing period in the query itself instead storing in a variable
        periods = {"weekly": "week", "monthly": "month"}
        if period not in periods:
            raise HTTPException(status_code=400, detail="wrong values filled")
        trunc = periods[period]
        # f string to call the period as a keyword in SQL
        await cur.execute(f"""
            SELECT date_trunc('{trunc}', clock_in) AS period_start,
                ROUND(EXTRACT(EPOCH FROM COALESCE (SUM(clock_out - clock_in), INTERVAL '0')) /3600, 2) AS total_hours
            FROM shifts
            WHERE worker_id=%s AND clock_out IS NOT NULL
            GROUP BY date_trunc('{trunc}', clock_in)
            ORDER BY date_trunc('{trunc}', clock_in) 
""", (worker_id,))
        computed_period = await cur.fetchall()
        return computed_period