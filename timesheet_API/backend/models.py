# the models file for pydantic models
from pydantic import BaseModel
from datetime import datetime

class ClientLogin(BaseModel):
    username: str
    password: str

class CreateWorkers(BaseModel):
    name: str
    username: str # authentication route
    password: str # authentication route

class UpdateEntry(BaseModel): # cannot put bare values as params so a model for the admin route
    clock_in: datetime | None=None
    clock_out: datetime | None=None