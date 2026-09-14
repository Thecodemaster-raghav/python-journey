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
from fastapi import FastAPI
from contextlib import asynccontextmanager
from psycopg_pool import AsyncConnectionPool
from psycopg.rows import dict_row
from config import database_conn
from workers import router as worker_routes
from shifts import router as shift_routes
from admin import router as admin_routes
from auth import router as auth_routes

@asynccontextmanager
async def lifespan(app: FastAPI):
    # opening up the connection to postgres
    # kwargs the argument is the dict of settings passed through, row_factory is the setting itself
    app.state.conn_pool = AsyncConnectionPool(database_conn,open=False,kwargs={"row_factory": dict_row})
    await app.state.conn_pool.open()
    yield
    # shutdown the connection
    await app.state.conn_pool.close()

app = FastAPI(lifespan=lifespan)
app.include_router(worker_routes)
app.include_router(shift_routes)
app.include_router(admin_routes)
app.include_router(auth_routes)