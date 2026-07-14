from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

app = FastAPI()

# a class called music
class Music(BaseModel):
    song_name : str
    song_type : str
    sung_by : str
    spotify_listeners : int
    song_id : int

def load_data():
    try:
        with open("music.json", "r", encoding="utf-8") as f:
            new_data = json.load(f)
    except FileNotFoundError:
        return []
    music_list = []
    for n in new_data:
        data_new = Music(**n)
        music_list.append(data_new)
    return music_list

musicians_list = load_data()

@app.get("/music")
def read_only():
    return musicians_list

@app.post("/music")
def create_data(music_file: Music):
    biggest = 0
    for m in musicians_list:
        if m.song_id > biggest:
            biggest = m.song_id
        music_file.song_id = biggest + 1
    musicians_list.append(music_file)
    save_data()
    return music_file
    

@app.put("/music/{song_id}")
def update_data(song_id: int, music_file: Music):
    if 0 <= song_id < len(musicians_list):
        musicians_list[song_id] = music_file
        save_data()
        return music_file
    else:
        raise HTTPException(status_code=404, detail="no songs found")

@app.delete("/music/{song_id}")
def del_data(song_id: int):
    if 0 <= song_id < len(musicians_list):
        del musicians_list[song_id]
        save_data()
        return {"success": "music data is deleted"}
    else:
        raise HTTPException(status_code=404, detail="no songs found")
    
# saving data now as a json file so that we do not loose data even though the server is not running
def save_data():
        new_data = []
        for m in musicians_list:
            new_data.append(m.model_dump())
        with open("music.json", "w", encoding="utf-8") as file:
            json.dump(new_data, file, indent=2)


# REST VOCAB polish for todays session post work:
# Resources: what is a resource? Why route /music and not /get_music or /cretae_song?

# Resource is the thing that exists and in our case it is the music files.
# and the URL is always a Noun never a verb and URL is path that names i want music files
# the methods like POST, GET, DELETE are the actions. and JSON is the copy of the resource
# response that travels through post, put request body -> this is called the representation.
# and representation is the copy of resource. In our case the music files 
# collection resource in patients API -> /patients
# the individual resource in patients api -> /patients/{patients_id}

# read or mutate routes in the 2 APIS /patients and /music:
# # SAFE : An operation is SAFE  that means. It only reads and changes nothing.
# Idempotent - meaning the final state stays the same even after performing any actions - that is idempotency.
# POST is the only state which is nt Idempotent in the API.
# Delete is idempotent in the final state: Meaning the at 1st call the removes the song.
# but calls from 2-5 hit the else and raie 404, but the system state after call 5
# equals to system state after 1: THE NUANCE: same state, different responses.
# one design limitation in the API of why the DELETE is not idempotent is because we check with 
# position or indexes not with having a value against every position.
# will build this tomorrow.

# the status codes that we give out as response
# like 200 means successful response and each number contracts a response attached to it.
# or someone who has never seen the code behind it.
# 2xx -> success, 4xx -> clients fault, 5xx -> server fault or internal server error
# FastAPI sends 200 as the default whenver the function returns normally.
# error 400 -> when the client fills out wrong information.
# error 404 -> the resource does not exist