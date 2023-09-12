import requests
import json

# Define the API endpoint 
url = 'http://localhost:8000/api/'  

# Define the data for the new user in the format expected by your API
data = {
    "name": "Junior",
}

# Send a POST request with JSON data and the appropriate headers
headers = {'Content-Type': 'application/json'}

try:
    response = requests.post(url, data=json.dumps(data), headers=headers)

    # Check the response
    if response.status_code == 201:
        print("User created successfully")
    else:
        print("Error:", response.status_code)
        print(response.content)
except requests.exceptions.RequestException as e:
    print("Error making the request:", str(e))
