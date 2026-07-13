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