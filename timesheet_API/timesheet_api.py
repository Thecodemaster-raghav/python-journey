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
from datetime import date
from contextlib import asynccontextmanager
import os
from psycopg_pool import AsyncConnectionPool
from dotenv import load_dotenv
from psycopg.rows import dict_row
from pydantic import BaseModel
import bcrypt
import jwt
from fastapi.security import HTTPBearer

load_dotenv() # loading the connection
database_conn = os.environ["DATABASE_URL"] # Connection string to postgres

# jwt_token reading from the .env file
jwt_secret = os.environ["JWT_SECRET"]

@asynccontextmanager
async def lifespan(app: FastAPI):
    # opening up the connection to postgres
    # kwargs the argument is the dict of settings passed through, row_factory is the setting itself
    app.state.conn_pool = AsyncConnectionPool(database_conn, kwargs={"row_factory": dict_row}) 
    yield
    # shutdown the connection
    await app.state.conn_pool.close()

app = FastAPI(lifespan=lifespan)
# creating an instance for the token dependency function
# header extraction using this function
security = HTTPBearer()

class ClientLogin(BaseModel):
    username: str
    password: str

class CreateWorkers(BaseModel):
    name: str
    username: str # authentication route
    password: str # authentication route

# hash password func using bcrypt
# gensalt() for random salt generation
# encode -> changes str to bytes and decode -> changes bytes to str for text readable format for database
# not an async because nothing is external just computations
def hash_password(password) -> bool:
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    return hashed_password

# verify or password check function
# using the -> bool to verify that the return values i going to be a boolean
def verify_pass(password, store_hash) -> bool:
    new_pass = bcrypt.checkpw(password.encode(), store_hash.encode())
    return new_pass

# dependency function for token check on the routes
# token dependency needs headers
# credentials is the actual token now and HTTPBearer is the instance we created to extract the header
def verify_tokens(token=Depends(security)) -> int:
    try: # try block to gracefully come of the program rather than shutting down the app
        decoded = jwt.decode(token.credentials, jwt_secret, algorithms=["HS256"])
        return decoded["worker_id"]
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token request")

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

# authentication register route
# design decision: having all the fields not null same as a production system. 
# which enables the clients using the register column, mandatory to fill in those fields.
@app.post("/register")
async def registerClient(register_data: CreateWorkers, auth=Depends(get_conn)):
    async with auth.cursor() as cur:
        await cur.execute("SELECT username FROM workers WHERE username=%s", (register_data.username,))
        auth_rows = await cur.fetchone()
        if auth_rows is not None:
            raise HTTPException(status_code=409, detail="username exists already")
        hashed = hash_password(register_data.password)
        await cur.execute("""
                INSERT INTO workers(name, username, hash_pass) VALUES (%s, %s, %s)
                RETURNING username, role
                """, (register_data.name, register_data.username, hashed,))
        register_rows = await cur.fetchone()
        return register_rows

# the login route which is POST not because it is creating a resource but because it carries sensitive data 
# as that of a password
@app.post("/login")
async def user_login(user_login: ClientLogin, login_conn=Depends(get_conn)):
    async with login_conn.cursor() as cur:
        # query by username
        await cur.execute("SELECT hash_pass, worker_id, role FROM workers WHERE username=%s", (user_login.username,))
        login_row = await cur.fetchone()
        if login_row is None:
            raise HTTPException(status_code=401, detail="wrong username or password")
        # verify_pass excepts 2 args one with password and the other is the stored hash_pass which we are checking against the 
        # pass at login
        check_pass = verify_pass(user_login.password, login_row["hash_pass"])
        if not check_pass:
            raise HTTPException(status_code=401, detail="wrong username or password")
         # login creates a token -> encode(), a protected route receives a token and checks it -> decode()
        create_token = jwt.encode({"worker_id": login_row["worker_id"]}, jwt_secret, algorithm="HS256")
        return {"access_token": create_token, "token_type": "bearer"}

# POST /shifts route with 2 gaurds where Guard 1 fails when it finds nothing (worker missing). 
# Guard 2 fails when it finds something (open shift exists).
# we get worker_id from the tokens itself now so need for the model for shift with worker id so that
# no other worker can edit other workers shift timings
@app.post("/shifts")
async def create_data(new_con= Depends(get_conn), current_worker=Depends(verify_tokens)):
    async with new_con.cursor() as cur:
        await cur.execute("SELECT worker_id FROM workers WHERE worker_id=%s", (current_worker,))
        fetch_worker_row = await cur.fetchone()
        if fetch_worker_row is None:
            raise HTTPException(status_code=404, detail="no matching workers found")
        await cur.execute("SELECT worker_id FROM shifts WHERE worker_id=%s AND clock_out IS NULL", (current_worker,))
        fetch_shift_row = await cur.fetchone()
        if fetch_shift_row is not None:
            raise HTTPException(status_code=409, detail="dual shift entry")
        await cur.execute("INSERT INTO shifts (worker_id, clock_in) VALUES (%s, now()) RETURNING *", (current_worker,))
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
        if clockOut_rows["clock_out"] is not None: # as the clockOut_rows is a dict row
            raise HTTPException(status_code=409, detail="clocked out exist already")
        await cur.execute("UPDATE shifts SET clock_out = now() WHERE shift_id=%s RETURNING *", (shift_id,)) # no insert 
        # as we are updating the table not inserting values
        clockOut_update = await cur.fetchone()
        return clockOut_update

# the aggregation route
# COALESCE is a SQL function that takes a list of values and returns the first one that isn't NULL
# WHAT extract epoch from does is that it extracts the number out of the interval and EPOCH from is what asking to give the
# total as seconds; /3600 is plain division 3600 is an hour so this converts seconds to hour
# add the 403 route for ownership check
@app.get("/workers/{worker_id}/hours")
# borrowing the connection
async def agg_hours(worker_id: int, hours_conn=Depends(get_conn), worker_tokens=Depends(verify_tokens)):
    async with hours_conn.cursor() as cur: # .cursor() creates a cursor on the connection
        await cur.execute("SELECT worker_id FROM workers WHERE worker_id=%s", (worker_id,)) # check againts no matching worker_id
        hour_rows = await cur.fetchone()
        if hour_rows is None:
            raise HTTPException(status_code=404, detail="no matching workers found")
        if worker_tokens != worker_id:
            raise HTTPException(status_code=403, detail="Access Forbidden")
        await cur.execute("""
        SELECT ROUND(EXTRACT(EPOCH FROM COALESCE(SUM(clock_out - clock_in), INTERVAL '0')) /3600, 2) AS total_hours
        FROM shifts 
        WHERE worker_id=%s AND clock_out IS NOT NULL
        """, (worker_id,))
        hours = await cur.fetchone()
        return hours 

# aggregation route to see hours weekly and monthly
# returning filtered date hours
# every non default signature goes first
@app.get("/workers/{worker_id}/breakdown")
async def breakdown_hours(worker_id: int, start: date , end: date, period: str ="weekly", hours_conn=Depends(get_conn)):
    async with hours_conn.cursor() as cur:
        await cur.execute("""
              SELECT worker_id 
              FROM workers 
              WHERE worker_id=%s                          
              """, (worker_id,))
        computed_row = await cur.fetchone()
        if computed_row is None:
            raise HTTPException(status_code=404, detail="no matching workers found")
# deploying a hanrdcoded dict instead of passing period in the query itself instead storing in a variable
        periods = {"weekly": "week", "monthly": "month"}
        if period not in periods:
            raise HTTPException(status_code=400, detail="wrong input value")
        trunc = periods[period]
        if start >= end:
            raise HTTPException(status_code=400, detail="wrong input date")
        # f string to call the period as a keyword in SQL
        # wrapped the date_trunc in to_char to format the timestamp into a readable string
        await cur.execute(f"""
        SELECT to_char(date_trunc('{trunc}', clock_in), 'YYYY Mon DD') AS period_start,
            ROUND(EXTRACT (EPOCH FROM COALESCE(SUM(clock_out - clock_in), INTERVAL '0')) /3600, 2) AS total_hours
        FROM shifts
        WHERE worker_id=%s AND clock_out IS NOT NULL AND clock_in >= %s AND clock_in < %s
        GROUP BY date_trunc('{trunc}', clock_in)
        ORDER BY date_trunc('{trunc}', clock_in)
        """, (worker_id, start, end,))
        period_rows = await cur.fetchall()
        return period_rows