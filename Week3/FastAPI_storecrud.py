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
    timestamp : datetime # needs a default as json not able to serialise datetime
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
        return [], 1
    new_data = [] # returning looping only one using a model param which decides hen called which model to choose
    for s in load_visit["visits"]:
        data = Visit(**s) # converting json to python args
        new_data.append(data)
    return new_data, load_visit["new_id"]

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


visits_list, new_id = load_data_visits("visits.json") # pass the class so function can initiate it N times in the loop 
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

# POST goal is to give a new store a permanent id from the counter, then save
@app.post("/stores") # reusing the next_id
def create_data(store: Store):
    global next_id  # reassigns the id
    store.store_id = next_id # this line reads
    next_id += 1
    stores_list.append(store)
    save_store_data()
    return store

# the method where we do deduplication of the code is called the DRY(donot repeat yourself) method 
# where we an just create a function (for future builds)
# so that we are not using a duplicate chunk of code and initiate that 
@app.post("/stores/{store_id}/visits")
def create_new_data(store_id: int):
    found = False # same checking program as that of GET
    for c in stores_list:
        if c.store_id == store_id:
            found = True
        if not found:
            raise HTTPException(status_code=404, detail="no store found")
    # building a visit object 

def save_store_data():
    store_data = []
    for l in stores_list:
        store_data.append(l.model_dump())
    data = {"store": store_data, "next_id": next_id}
    with open("stores.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def save_visit_data():
    visit_data = []
    for v in visits_list:
        visit_data.append(v.model_dump())
    v_data = {"visits": visit_data, "new_id": new_id}
    with open("visits.json", "w", encoding="utf-8") as file:
        json.dump(v_data, file, indent=2)