# prediction.py

from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
import joblib

# Load your existing model (do not change the file name)
with open("best_model_LinearRegression.pkl", "rb") as f:
    model = joblib.load(f)

app = FastAPI(title="Linear Regression Prediction API", version="0.1")

# Enable CORS for any origin (safe for demo; in production, restrict it)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input data schema with Pydantic
class PredictionInput(BaseModel):
    feature1: float = Field(..., ge=0, description="Feature1 must be ≥ 0")
    feature2: float = Field(..., ge=0, description="Feature2 must be ≥ 0")
    feature3: float = Field(..., ge=0, description="Feature3 must be ≥ 0")

@app.post("/predict")
def predict(input: PredictionInput):
    features = [[input.feature1, input.feature2, input.feature3]]
    prediction = model.predict(features)[0]
    return {"prediction": float(prediction)}

# Placeholder for retraining endpoint
@app.post("/retrain")
def retrain():
    return {"message": "Retraining endpoint placeholder. Upload new data to trigger retraining."}

@app.get("/")
def root():
    return {"message": "Linear Regression Prediction API is running"}