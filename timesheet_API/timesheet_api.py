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

from fastapi import FastAPI
import os
from dotenv import load_dotenv
from contextlib import asynccontextmanager
from psycopg_pool import AsyncConnectionPool
from psycopg.rows import dict_row

load_dotenv() # loads the file into the environment
database_conn = os.environ["DATABASE_URL"] # connection string for postgres

@asynccontextmanager # the decoratore for the lifespan
async def lifespan(app: FastAPI): # the lifespan itself
    # inside the lifespan above the yield is the pool creation
    # state an attribute FastAPI provides for storing anything that needs to live for the whole app and be reachable
    app.state.conn_pool = AsyncConnectionPool(database_conn) 
    yield
    # below yield is the shutdown code
    await app.state.conn_pool.close() # shutsd own the pool and releses the connection so no stale connection process linger


app = FastAPI(lifespan=lifespan)
