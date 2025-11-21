import requests
import json
from datetime import datetime
import base64
import time
 
# Configuration
API_URL = "https://bosch-iot-insights.com/data-recorder-service/v2/poq7695"  # Replace with your actual endpoint
USERNAME = "poq7695-wahxbw-api"         # Replace with your API username
PASSWORD = "Ms-8gmbzdaPlzKpf"         # Replace with your API password
 
def send_dummy_data():
    # Prepare the data payload
    payload = {
        "transformer_id": "transformer_1",
        "time": datetime.now().isoformat(),  # Current time in ISO format
        "temperature": 26.0
    }
    # Create basic auth header
    credentials = base64.b64encode(f"{USERNAME}:{PASSWORD}".encode()).decode()
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {credentials}"
    }
    try:
        # Send POST request
        response = requests.post(
            API_URL,
            data=json.dumps(payload),
            headers=headers,
            timeout=30
        )
        # Check response
        if response.status_code == 200:
            print("✅ Data sent successfully!")
            print(f"Response: {response.text}")
        else:
            print(f"❌ Failed to send data. Status code: {response.status_code}")
            print(f"Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error occurred: {e}")
 
if __name__ == "__main__":
    while True:
        send_dummy_data()
        time.sleep(300)
