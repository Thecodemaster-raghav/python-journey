# secret and the enviroment
import os
from dotenv import load_dotenv

load_dotenv() # loading the connection
database_conn = os.environ["DATABASE_URL"] # Connection string to postgres

# jwt_token reading from the .env file
jwt_secret = os.environ["JWT_SECRET"]