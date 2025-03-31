# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app
COPY failure_prediction_model.pkl /app  

# Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn pandas joblib scikit-learn

# Expose port for FastAPI
EXPOSE 8000

# Command to run the FastAPI app
CMD ["uvicorn", "fastapi_k8s_failure_api:app", "--host", "0.0.0.0", "--port", "8000"]
