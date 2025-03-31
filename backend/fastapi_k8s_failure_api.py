from fastapi import FastAPI
import pickle
import numpy as np
import pandas as pd
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

# Load the trained model
with open("failure_prediction_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Load dataset to get median values for normalization
df = pd.read_csv("/content/boa_dataset_ml_ready_frontend_microservice.csv", encoding="utf-8")
selected_features = [
    'container_memory_working_set_bytes',
    'container_memory_usage_bytes',
    'container_file_descriptors',
    'container_network_receive_bytes_rate',
    'total_header_bytes'
]
feature_medians = df[selected_features].median().to_dict()  # Store median values for preprocessing

# Define request format
class Features(BaseModel):
    container_memory_working_set_bytes: float
    container_memory_usage_bytes: float
    container_file_descriptors: float
    container_network_receive_bytes_rate: float
    total_header_bytes: float

@app.post("/predict")
def predict_failure(data: Features):
    # Normalize input using median from training data
    input_data = np.array([
        data.container_memory_working_set_bytes - feature_medians['container_memory_working_set_bytes'],
        data.container_memory_usage_bytes - feature_medians['container_memory_usage_bytes'],
        data.container_file_descriptors - feature_medians['container_file_descriptors'],
        data.container_network_receive_bytes_rate - feature_medians['container_network_receive_bytes_rate'],
        data.total_header_bytes - feature_medians['total_header_bytes']
    ]).reshape(1, -1)

    # Make prediction
    prediction = model.predict(input_data)

    return {"prediction": prediction.tolist()}
