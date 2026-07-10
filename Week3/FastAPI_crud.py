# a working CRUD API for medicine
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
patients_data = []
recommended_meds = {"fever": "paracetamol", "cough": "syrup", "cold": "tynol"}

# a class called patient to post patients data
class Patient(BaseModel):
    patient_name : str
    age : int
    sickness_type : str
    medication_type : str
    

# post data: creating and storing patients data
# adding a layer of error handling on our api's post, put, del as we want the errors to be said out loud.
# we will raise the errors not return them in else block of the code.
@app.post("/patients")
def create_data(data: Patient):
    new_data = recommended_meds.get(data.sickness_type) # this throws off the None the .get() on a dict
    patients_data.append(data)
    if new_data is not None:
        correct_meds = new_data == data.medication_type
        # if None is returned raise the error and if not None work the code.
        return {"patient_Info": data, "correct_medication": correct_meds}
    else:
        return {"error": "no sickness found"}

@app.get("/patients")
def read_data():
    return patients_data

# adding the error handling layer 

@app.put("/patients/{patient_id}")
def update_data(patient_id: int, data: Patient):
    if patient_id < len(patients_data): # this is the edge case for the out of bounds error
        patients_data[patient_id] = data
        return data
    else:
        raise HTTPException(status_code=404, detail="patient not found")
    
@app.delete("/patients/{patient_id}")
def delete_data(patient_id: int):
    if patient_id < len(patients_data):
        del patients_data[patient_id]
        return {"success": "patients data is deleted"}
    else:
        raise HTTPException(status_code=404, detail="patient not found")
    
# we use 404 error code where theere is some resource is missing and 
# using 400 on post as the request has unusable data itself.