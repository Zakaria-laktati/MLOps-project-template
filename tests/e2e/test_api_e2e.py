from fastapi import FastAPI
import requests

app = FastAPI()

# Replace with your actual model endpoint
MODEL_ENDPOINT = "http://localhost:8000/predict"

@app.get("/")
def read_root():
    return {"message": "Welcome to the ML API"}

@app.post("/predict")
def predict(data: dict):
    response = requests.post(MODEL_ENDPOINT, json=data)
    return response.json()