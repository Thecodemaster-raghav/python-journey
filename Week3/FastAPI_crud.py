# a working CRUD API for medicine
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

app = FastAPI()

# a class called patient to post patients data
class Patient(BaseModel):
    patient_name : str
    age : int
    sickness_type : str
    medication_type : str

recommended_meds = {"fever": "paracetamol", "cough": "syrup", "cold": "tynol"}

def load_data():
    try:
        with open("patients.json", "r", encoding="utf-8") as f:
            now_data = json.load(f)
    except FileNotFoundError:
        return []
    data_load = []
    for n in now_data:
        data_back = Patient(**n)
        data_load.append(data_back)
    return data_load

patients_data = load_data()

# post data: creating and storing patients data
# adding a layer of error handling on our api's post, put, del as we want the errors to be said out loud.
# we will raise the errors not return them in else block of the code.
# but here i have deliberatly left out for raising the error as i want to save the data even the 
# reccomended_meds do not match
@app.post("/patients")
def create_data(data: Patient):
    new_data = recommended_meds.get(data.sickness_type)
    patients_data.append(data)
    save_data()
    if new_data is not None:
        correct_medication = new_data == data.medication_type
        return {"patients": data, "correct_meds": correct_medication}
    else:
        return {"error": "no sickness found"}
    

@app.get("/patients")
def read_data():
    return patients_data

# adding the error handling layer 
# handling the non negative edge where the value entered by the client should not be a -ve value
@app.put("/patients/{patient_id}")
def update_data(patient_id: int, data: Patient):
    if 0 <= patient_id < len(patients_data): # this is the edge case for the out of bounds error
        patients_data[patient_id] = data
        save_data()
        return data
    else:
        raise HTTPException(status_code=404, detail="patient not found")

# handling the non negative edge where the value entered by the client should not enter a -ve value
@app.delete("/patients/{patient_id}")
def delete_data(patient_id: int):
    save_data()
    if 0 <= patient_id < len(patients_data):
        del patients_data[patient_id]
        save_data()
        return {"success": "patients data is deleted"}
    else:
        raise HTTPException(status_code=404, detail="patient not found")
    
# we use 404 error code where theere is some resource is missing and 
# using 400 on post as the request has unusable data itself.
# 0 <= x <= len is a idomatic way of python to express that x is a valid integer. 

# now the prsitence check. loading and saving data even after server restart
def save_data():
    data_list = []
    for p in patients_data: # looping over patients_data to turn the list of patient objects into a list of dicts
        data_list.append(p.model_dump())
    with open("patients.json", "w", encoding="utf-8") as file:
        json.dump(data_list, file, indent=2)