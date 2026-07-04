# a small throwaya lookup server
# the design: The data will look like a dict of movie recocomendation
# where we will have director, name, genre and ratings 
# will have one path param route which will fetch the data using name and genre of the movie
# will also have a query param to filter out movies using ratings. {} will go to the path params
# and query param will have a rating route that will filter the list of a movies and that is followed by
# a ?. Will have genre and ratings limit as wuery params to filter the data.

from fastapi import FastAPI

app = FastAPI()
movies_data = [
        {"movie_id": 1, "name": "Interstellar", "director": "christopher nolan", "genre": "SCI-FY", "ratings": 8.6},
        {"movie_id": 2, "name": "BirdBox", "director": "Susanne Bier", "genre": "sensory horror", "ratings": 6.9},
        {"movie_id": 3, "name": "MoneyBall", "director": "Bennett Miller", "genre": "sports", "ratings": 8.5},
        {"movie_id": 4, "name": "Dhurandhar", "director": "Aditya Dhar", "genre": "action", "ratings": 9.0},
        ]

# route on with the data and movie_id's
@app.get("/movies/{movie_id}")
def read_data(movie_id: int):
    for i in movies_data:
        if i["movie_id"] == movie_id:
            return i
    return {"Error: movie_id not found"}

# now filtering with query params
@app.get("/filter")
def filter_data(genre, min_rating: float=0.0):
    result = []
    for n in movies_data:
        if n["genre"] == genre and n["ratings"] >= min_rating:
            result.append(n)
    return result
    