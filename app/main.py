from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# Load the trained model
MODEL_PATH = "app/linear_regression_model.pkl"
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

app = FastAPI()

# Define the input schema
class PredictionInput(BaseModel):
    years_experience: float

latest_prediction = {"years_experience": None, "predicted_salary": None}

# Define the API endpoint for prediction
@app.post("/predict/")
async def predict(data: PredictionInput):
    global latest_prediction
    input_data = np.array(data.years_experience).reshape(1, -1)  # Reshape for prediction
    predicted_salary = round(model.predict(input_data)[0], 2)  # Make prediction
    latest_prediction = {
        "years_experience": data.years_experience,
        "predicted_salary": predicted_salary,
    }
    return latest_prediction

@app.get("/")
def result():
    if latest_prediction["years_experience"] is None:
        return {"message": "No prediction has been made yet."}
    return latest_prediction
