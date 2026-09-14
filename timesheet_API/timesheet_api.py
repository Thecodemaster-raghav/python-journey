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
from fastapi import FastAPI, Depends, HTTPException
from datetime import date
from contextlib import asynccontextmanager
from psycopg_pool import AsyncConnectionPool
from psycopg.rows import dict_row
from config import database_conn, jwt_secret
from dependencies import get_conn, verify_tokens, hash_password, verify_pass
import jwt
from models import ClientLogin, CreateWorkers, UpdateEntry
from workers import router as worker_routes
from shifts import router as shift_routes

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

# admin GET route
@app.get("/admin")
async def admin_shifts(conn_admin=Depends(get_conn), tokens=Depends(verify_tokens)):
    async with conn_admin.cursor() as cur:
        await cur.execute("SELECT role FROM workers WHERE worker_id=%s", (tokens,))
        caller = await cur.fetchone()
        if caller is None:
            raise HTTPException(status_code=404, detail="Invalid Entry")
        if caller["role"] != "admin":
            raise HTTPException(status_code=403, detail="Access Forbidden")
        await cur.execute("SELECT * FROM shifts")
        rows = await cur.fetchall()
        return rows 

# authentication register route
# design decision: having all the fields not null same as a production system. 
# which enables the clients using the register column, mandatory to fill in those fields.
@app.post("/register")
async def register_worker(register_data: CreateWorkers, auth=Depends(get_conn)):
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
async def login(user_login: ClientLogin, login_conn=Depends(get_conn)):
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

# admin route for updating or changing the clock-in clock-out times for workers
# query the callers role; 403 if not admin
@app.patch("/admin/{shift_id}")
async def update_entry(entry: UpdateEntry, shift_id: int, conn=Depends(get_conn), tokens=Depends(verify_tokens)):
    async with conn.cursor() as cur:
        await cur.execute("SELECT role FROM workers WHERE worker_id=%s", (tokens,))
        rows = await cur.fetchone()
        if rows is None:
            raise HTTPException(status_code=404, detail="Invalid Entry")
        if rows["role"] != "admin":
            raise HTTPException(status_code=403, detail="Access Forbidden")
        # for the dynamic UPDATE the in the admin fields
        pieces = []
        values = []
        if entry.clock_in is not None:
            pieces.append("clock_in=%s") # holds string
            values.append(entry.clock_in) # holds data
        if entry.clock_out is not None:
            pieces.append("clock_out=%s")
            values.append(entry.clock_out)
        if not pieces:
            raise HTTPException(status_code=400, detail="Invalid Entry")
        # putting the pieces together with join
        # clock_in , clock_out as strings
        joined_pieces = (",").join(pieces)
        await cur.execute(f"UPDATE shifts SET {joined_pieces} WHERE shift_id=%s RETURNING *", values + [shift_id],)
        admin_rows = await cur.fetchone()
        return admin_rows 