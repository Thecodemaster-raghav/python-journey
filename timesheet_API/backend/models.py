# the models file for pydantic models
from pydantic import BaseModel, Field
from datetime import datetime
from decimal import Decimal

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

class RateUpdate(BaseModel):
    hourly_rate: Decimal=Field(gt=0,max_digits=10, decimal_palces=2) # for calculating thr pay