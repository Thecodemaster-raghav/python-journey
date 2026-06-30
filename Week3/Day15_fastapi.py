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

@app.get("/afford/{amount}")
def calc_budget(amount):
    if int(amount) < 1000:
        user_budget = {"amount": int(amount), "affordable": True}
    elif int(amount) >= 1000:
        user_budget = {"amount": int(amount), "affordable": False}
    return user_budget

