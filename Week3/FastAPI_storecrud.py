# Making a API which takes the amount of people visits the store per day and finds out 
# when is the most busiest time of the day for the stores to employ schemes and techniques to increase
# traffic at the other time of the day. Collects data and this api can be used for data analysis purposes.

# Part - 1: Design:
# the design holds 2 resources, visit and a store where a visit is an event belonging to a store.

# Two field visit record - timestamp and store_id -> minimal design
# there is a NOISE IN THE SIGNAL constraint which can calculate the wrong data; like bot traffic in web
# test transactions in payment data. and in my case that the sensor records events taht are not customers
# so the aggregations will lie. 
# but the counts include staff movement; acceptable for v1

# the Store field holds: name and store_id
# the API design pattern holds: POST /stores/{store_id}/visits -> a nested route. 
# Orphan prevension by refusal: which means to prevent the delete from deleting the whole of 200 rows of data
# since we are using nesting DELETE /stores/3 and if store 3 has 200 visits recorded.
# so in defence of that asking the client if they are sure if they want to delete the data.
from fastapi import FastAPI
from pydantic import BaseModel
import json
from datetime import datetime

app = FastAPI()

class Visits(BaseModel):
    timestamp : datetime.now
    store_id : int
    visit_id : int | None = None

class Stores(BaseModel):
    name : str
    store_id : int | None = None