# a working CRUD API for medicine
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
patients_data = []
recommended_meds = {"fever": "paracetamol", "cough": "syrup"}

# a class called patient to post patients data
class Patient(BaseModel):
    patient_name : str
    age : int
    sickness_type : str
    medication_type : str
    

# post data: creating and storing patients data
@app.post("/patients")
def create_data(data: Patient):
    new_data = recommended_meds.get(data.sickness_type)
    if new_data is not None:
        correct_medication = new_data == data.medication_type
        patients_data.append(data)
        return {"patient":data, "correct_medication": correct_medication}
    else:
        return {"no reccomendation available for this sickness"}

@app.get("/patients")
def read_data():
    return patients_data


@app.put("/patients/{patient_id}")
def update_data(patient_id: int, data: Patient):
    if patient_id < len(patients_data):
        patients_data[patient_id] = data
        return data
    else:
        return {"error": "patient not found"}
    
@app.delete("/patients/{patient_id}")
def delete_data(patient_id: int):
    if patient_id < len(patients_data):
        del patients_data[patient_id]
        return {"patients data is deletd"}
    else:
        return {"No patient found"} 