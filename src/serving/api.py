from pathlib import Path
from typing import List

import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


MODELS_DIR = Path("models")
MODEL_PATH = MODELS_DIR / "regression_model.joblib"

app = FastAPI(title="Regression API", version="0.1.0")

model = None


class PredictionRequest(BaseModel):
    features: List[float]


@app.on_event("startup")
def load_model():
    global model
    if MODEL_PATH.exists():
        model = joblib.load(MODEL_PATH)
    else:
        model = None


@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": model is not None}


@app.post("/predict")
def predict(request: PredictionRequest):
    if model is None:
        return {"error": "Model not loaded"}
    prediction = model.predict([request.features])[0]
    return {"prediction": float(prediction)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), 'model.joblib')
model = joblib.load(model_path)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([data['features']])
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)