from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

# Load the trained model
model = joblib.load("anomaly_model.pkl")

app = FastAPI()

class SensorData(BaseModel):
    volume: float
    weight: float

@app.post("/predict")
def predict(data: SensorData):
    input_data = np.array([[data.volume, data.weight]])
    prediction = model.predict(input_data)
    result = "Anomaly" if prediction[0] == -1 else "Normal"
    return {"prediction": result}
