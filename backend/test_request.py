import json
import requests
import requests
import json

# Define the API URL
API_URL = "http://127.0.0.1:8000/predict"

# Generate dummy feature values (Replace with real values)
data = {
    "container_memory_working_set_bytes": 12345.67,
    "container_memory_usage_bytes": 54321.89,
    "container_file_descriptors": 250.0,
    "container_network_receive_bytes_rate": 9876.54,
    "total_header_bytes": 4567.89
}

# Send the POST request
response = requests.post(API_URL, json=data)

# Print the response
print("Status Code:", response.status_code)
try:
    print("Response JSON:", response.json())
except json.JSONDecodeError:
    print("Invalid JSON response:", response.text)
