# starting with fast api and running with uvicorn it's server.
# First End point: piece 1: creating an app object
from fastapi import FastAPI

app = FastAPI() # when we do FastAPI() we are creating an instance of the FastAPI class

# Piece 2: defining the route with a decorator
@app.get("/")
def my_transaction(): # the route function takes no parameteres
    transaction = {"user": "raghav", "amount_debited": 6000}
    return transaction

my_transaction()
# we never call the function directly the server calls it when a visit arrives
# the wrapping/registering happens once up front; then each visit triggers the function 
# and its return value becomes the resonse. it returns the data as JSON file format
# browser-> sends for Requests -> Server sends back the response.
# request goes in and Server sends a (response) comes out.
# .get is the show me the data kind of label on the function
#  that we make to a server and it sends out a reponse.
# localhost is the address where the server is sitting.
# and the numbers that localhost uses are the ip addresses