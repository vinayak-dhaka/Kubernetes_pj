from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pickle
import numpy as np
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (change this in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Load the trained model
with open("failure_prediction_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Define request format
class Features(BaseModel):
    container_memory_working_set_bytes: float
    container_memory_usage_bytes: float
    container_file_descriptors: float
    container_network_receive_bytes_rate: float
    total_header_bytes: float

@app.post("/predict")
def predict_failure(data: Features):
    # Convert input to NumPy array
    input_data = np.array([
        data.container_memory_working_set_bytes,
        data.container_memory_usage_bytes,
        data.container_file_descriptors,
        data.container_network_receive_bytes_rate,
        data.total_header_bytes
    ]).reshape(1, -1)

    # Make prediction
    prediction = model.predict(input_data)

    return {"prediction": prediction.tolist()}
