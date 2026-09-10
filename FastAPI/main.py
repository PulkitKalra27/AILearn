from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as d:
        data = json.load(d)
    return data

@app.get('/')
def hello():
    return {"message": "Patient Management System API"}

@app.get('/about')
def about():
    return {"message":"API to manage patient records."}

@app.get('/view')
def view():
    data = load_data()
    return data