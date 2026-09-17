# all login and register routes
from fastapi import APIRouter, HTTPException, Depends
from models import CreateWorkers, ClientLogin
from dependencies import get_conn, hash_password, verify_pass, verify_tokens
import jwt
from config import jwt_secret
router = APIRouter()

# authentication register route
# design decision: having all the fields not null same as a production system. 
# which enables the clients using the register column, mandatory to fill in those fields.
@router.post("/register")
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
@router.post("/login")
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

# the delete route using transcation: hard delete
@router.delete("/account")
async def delete_account(conn=Depends(get_conn), token=Depends(verify_tokens)):
    async with conn.transaction():
        async with conn.cursor() as cur:
            await cur.execute("DELETE FROM shifts WHERE worker_id=%s", (token,))
            await cur.execute("DELETE FROM workers WHERE worker_id=%s", (token,))
            return {"delete_request": "success"}