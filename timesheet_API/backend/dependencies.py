# For the dependencies injections
import jwt
from fastapi.security import HTTPBearer
from fastapi import Request, Depends, HTTPException
from config import jwt_secret
import bcrypt

# creating an instance for the token dependency function
# header extraction using this function
security = HTTPBearer()

# dependency function : same shape as of the lifespan function but at a smaller scale
async def get_conn(request: Request):
    async with request.app.state.conn_pool.connection() as conn: # as this is a connection not a pool
        yield conn

# hash password func using bcrypt
# gensalt() for random salt generation
# encode -> changes str to bytes and decode -> changes bytes to str for text readable format for database
# not an async because nothing is external just computations
def hash_password(password) -> str:
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