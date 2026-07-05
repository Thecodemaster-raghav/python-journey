# now the post request with a request body. That enables clinet create something 
# not only just look things up.
# get is safe and is a ready only data no changes made to the server.
# while POST creates or changes data and does also makes changes to the server.
# A pydantic model lets us automatically validate and also converts type of the,
# entire incoming POST request body.
from pydantic import BaseModel # basemodel is a class that pydantic has with all the validation and type conversions
from fastapi import FastAPI
# the class movie inherits from Basemodel as then it will have all its pre-requisites by default and we 
# would not have to write them again an d again. 
# # Analogy: Like in a kitchen we have all the tools
# just peple using it changes not the tools instilled in it.

app = FastAPI()

class Movie(BaseModel):
    name : str
    director : str
    ratings : float

# the new syntax: app.post()

@app.post("/movies")
def create_movie(movie: Movie):
    return movie # this will return the name director and ratings with validation and type conversion 
# inherited from the BaseModel