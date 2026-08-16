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
    #kwargs the argument is the dict of settings passed through, row_factory is the setting itself
    app.state.conn_pool = AsyncConnectionPool(database_conn, kwargs={"row_factory": dict_row}) 
    yield
    # shutdown the connection
    await app.state.conn_pool.close()

app = FastAPI(lifespan=lifespan)

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


# POST /shifts route
@app.post("/shifts")
async def create_data(create_shift: CreateShift, new_con= Depends(get_conn)):
    async with new_con.cursor() as cur:
        await cur.execute("SELECT worker_id FROM workers WHERE worker_id=%s", (create_shift.CreateShift))
        