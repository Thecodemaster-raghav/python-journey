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

# aggregations over time: means counting events grouped by some slice of the timetamp.
@app.get("/stores/{store_id}/peak-hours")
def data_agg(store_id: int):
    new_data = [] # for collecting the hours.
    hour_data = {}
    highest_count = 0
    best_hour = None # edge case if no visit happens to the store
    match_id(store_id) # signature mismatches are always a TypeError
    for i in visits_list: # getting the hours from the timestamp using loop and the collecting them in the list
        if i.store_id == store_id:
            hour = i.timestamp.hour
            new_data.append(hour)
    for e in new_data: # building a dict to map the hours and count
        if e in hour_data:
            hour_data[e] += 1
        else:
            hour_data[e] = 1
    for k,v in hour_data.items(): # to get the best hour and highest no of visits
        if v > highest_count:
            best_hour = k
            highest_count = v
    return {"best_hour":best_hour, "highest_count": highest_count}


# this is an event log timestamped facts about things that have happened 
# in data engineering vocab: a store is a DIMENSION and a visit is FACT
@app.get("/stores/{store_id}/visits") # filter by store visits to the matching id from the visits to url
def read_data(store_id: int):
    new_list = []
    match_id(store_id)
    for r in visits_list:
        if r.store_id == store_id:
            new_list.append(r)
    return new_list

# POST goal is to give a new store a permanent id from the counter, then save
# store is the reference data of the entities that exists
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
    global new_id # reassigns the new_id
    match_id(store_id)
    # builduing the visit obj
    visit_obj = Visit(store_id=store_id, timestamp=datetime.now(), visit_id=new_id)
    new_id += 1 # incrementing the new_id; a conuter
    visits_list.append(visit_obj) # saving the obj in the list for it
    save_visit_data()
    return visit_obj

# Delete operation: 
# using status_code 409 conflict: meaning the same request that could change later without changing it,
# that is a 409 request
# shape of the design match_id(stores) -> raise 404 if exception, visit_list scan raise 409 if absent
# 3rd step -> actual removal
# step 4: persistence using save_
# step 5: walk the list and identify which element carries that store_id 
# and asign a variable to .remove(n) which would e an object nt an int against stores_list
@app.delete("/stores/{store_id}")
def delete_data(store_id: int):
    holds_obj = None
    has_visits = False
    match_id(store_id)
    for n in visits_list:
        if n.store_id == store_id:
            has_visits = True
    if has_visits: # BLOCKER which we need to not delete the visits
        raise HTTPException(status_code=409, detail="matching id found; no deletion")

def save_store_data():
    store_data = []
    for l in stores_list:
        store_data.append(l.model_dump())
    data = {"stores": store_data, "next_id": next_id}
    with open("stores.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

# to serialize the mode arguments can be set to 'json' to ensure json compatile types are used 
# an in our case we have a datetime value to serialise so will use mode='json'
def save_visit_data():
    visit_data = []
    for v in visits_list:
        visit_data.append(v.model_dump(mode='json')) # to make the values compatible to json
    v_data = {"visits": visit_data, "new_id": new_id}
    with open("visits.json", "w", encoding="utf-8") as file:
        json.dump(v_data, file, indent=2)

# refactoring: finding the matching store id as of the URL
def match_id(store_id):
    correct = False # false at the start; only true if the match is found in stores loop
    for n in stores_list:
        if n.store_id == store_id:
            correct = True # to check whether the store exists; that is passed in the URL
    if not correct: # and store_id not found raise an exception
        raise HTTPException(status_code=404, detail="no matching stores found")
    
    
# signature mismatches are always TyepError and an uncaught exception is always 5xx -> internal sever error
# which means the code is wrong but this gets missed in FastAPI.
# 4xx is clients fault

# the design pattern and choice for delete
# cascade: A delete that propogates. Meaning if you remove the parent and everything pointing
# at the parent gets deleted too automatically
# for refuse and cascade we are applying this rule to refuse if deleting would destroy
# analytic data
# and store exisiting is what this decision possible, but if the visit is there than that would 
# make it harmful for us to delete because deleting a visit would directly impact the analytical data
# so when a store has 0 visits and that nothing went downstream no visit exists.
# So nothing to protect; In that case the delte should succeed