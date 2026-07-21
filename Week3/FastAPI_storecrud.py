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
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
from datetime import datetime

app = FastAPI()

class Visit(BaseModel):
    timestamp : datetime.now # needs a default as json not able to serialise datetime
    store_id : int
    visit_id : int | None = None

class Store(BaseModel):
    name : str
    store_id : int | None = None

def load_data_visits(filename): # the edge case for error handling
    try:
        with open(filename, "r") as newfile:
            load_visit = json.load(newfile)
    except FileNotFoundError:
        return []
    new_data = [] # returning looping only one using a model param which decides hen called which model to choose
    for s in load_visit:
        data = Visit(**s) # converting json to python args
        new_data.append(data)
    return new_data

def load_data_stores(filename): # loads data for the store as a design choice; as the type is different to
    # that of the visit as we load visits as a list and store as a dict
    try:
        with open(filename) as file:
            load_store = json.load(file)
    except FileNotFoundError:
        return [], 1
    stores_data = []
    for t in load_store["stores"]:
        data = Store(**t) # converting json to python args
        stores_data.append(data)
    return stores_data, load_store["next_id"]


visits_list = load_data_visits("visits.json") # pass the class so function can initiate it N times in the loop 
# that is why no single empty object.
stores_list, next_id = load_data_stores("stores.json") 

@app.get("/store") # reading the data for stores
def read_stores():
    return stores_list

@app.get("/visits") # reading the visit data
def read_visits():
    return visits_list

@app.get("/stores/{store_id}/visits") # filter by store visits to the matching id from the visits to url
def read_data(store_id: int):
    new_list = []
    exists = False # false at the start; only true if the match is found in stores loop
    for s in stores_list:
        if s.store_id == store_id: # to check if url store_id matching the store_id in the list if not 
            exists = True # have a varibale with a boolean value that return whether true or false 
        if not exists: # and store_id not found raise an exception
            raise HTTPException(status_code=404, detail="no store present")
    for r in visits_list:
        if r.store_id == store_id:
            new_list.append(r)
    return new_list
        
@app.post("/stores") # reusing the 
def create_data(stores: Store):

