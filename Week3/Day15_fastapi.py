# starting with fast api and running with uvicorn it's server.
# First End point: piece 1: creating an app object

# we never call the function directly the server calls it when a visit arrives
# the wrapping/registering happens once up front; then each visit triggers the function 
# and its return value becomes the resonse. it returns the data as JSON file format
# browser-> sends for Requests -> Server sends back the response.
# request goes in and Server sends a (response) comes out.
# .get is the show me the data kind of label on the function
#  that we make to a server and it sends out a reponse.
# localhost is the address where the server is sitting.
# and the numbers that localhost uses are the ip addresses

from fastapi import FastAPI

app = FastAPI() # when we do FastAPI() we are creating an instance of the FastAPI class

# Piece 2: defining the route with a decorator
@app.get("/")
def my_transaction(): # the route function takes no parameteres
    transaction = {"user": "raghav", "amount_debited": 6000}
    return transaction
# the web app has different routes. We worked with the "/" homepage route yesterday
# today we will introduce a new route called "/savings" for the server to accept requests through that route
# using "/savings". Thing to notice here is that @app.get("...")-> this is what makes each route distinct.
# so "/savings " will be a different address.

@app.get("/savings")
def amount_saved():
    total_amount = 2600
    travel_spendings = 1200
    count_total = {"savings_left": total_amount - travel_spendings}
    return count_total

# Path parameters: a path param is a variable name in the URL that we type with curly braces in the route
@app.get("/user/{name}") # same route but different data driven by the URL
def user_name(name):
    user_now = {"user": name, "jersey": 7}
    return user_now

@app.get("/double/{number}")
def compute(number):
    now_total = int(number) * 2
    return now_total
# we have to convert the input not the output. As URL values always arrive as string

# to return the result as the labeled dict
@app.get("/square/{num}")
def squared(num):
    calc_squares = int(num) * int(num) # always do type conversion before the output.
    now_result = {"result": calc_squares} 
    return now_result
# term to lock in : A string is a sequence

# a route to tell the user abot the affordability
@app.get("/afford/{amount}")
def calc_budget(amount):
    if int(amount) < 1000: # type conversion has to happen at input.
        user_budget = {"amount": int(amount), "affordable": True}
    elif int(amount) >= 1000: # one thing to keep in mind is that the elif condition is gauranteed true.
        user_budget = {"amount": int(amount), "affordable": False}
    return user_budget

# Fast api- Next part: query params
# it looks like /items?limit=10
# here /items is the path meaning the route or room from which we are knocking from.
# now the query param which is ?limit=10 so here key is limit and value is 10
# and if we want to send more tha 1 we just join them with &
# so it looks like /items?limit=10&skip=5 that is two query params

@app.get("/items")
def read_items(limit=20): # here we will be falling back to 20 as default as nothing is passed.
    return limit # this is a query param as there is nothing passed between {} and so the URL wuld look like
     # /items?limit=20
     # return the dict which is limit.

# exercises:
@app.get("/greet")
def user_name(name):
    return {"Hello": name}

# two query params at once:
@app.get("/search")
def user_search(keyword, limit: int=10): # in here the default value of limit is set as 10 but user can pass any value.
    return {"keyword": keyword, "limit": limit, "type": type(limit).__name__}

# part 3: the type gotcha revisit:
# the same thing with the path params the URL converts the values as a stringeven though it is an int.

# part 4:
@app.get("/user/{user_id}/items") # the user_id sits in {} because it is part of the path
def users(user_id: int, limit: int =10):
    data = {"user_id": user_id, "limit": limit}
    return data

# async is used if we ever wait for something inside the function.
# async is a way to write functions that can pause while waiting for something like slow.
# and let the server do the work in the maintime, instead of sitting frozen.

# now the post request with a request body. That enables clinet create something 
# not only just look things up.
# get is safe and is a ready only data no changes made to the server.
# while POST creates or changes data and does also makes changes to the server.
# A pydantic model lets us automatically validate and also converts type of the,
# entire incoming POST request body.
