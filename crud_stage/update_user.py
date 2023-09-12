import requests
import json

# Define the base URL of your API
base_url = 'http://localhost:8000/api/'

# Function to update user details
def update_user(user_id, updated_data):

    # Define the endpoint for updating user details
    endpoint = f'{base_url}{user_id}/'

    try:
        # Send a PUT request with updated data
        response = requests.put(endpoint, data=json.dumps(updated_data), headers={'Content-Type': 'application/json'})

        # Check the response
        if response.status_code == 200:
            print("User details updated successfully")
        elif response.status_code == 404:
            print("User not found")
        elif response.status_code == 400:
            print("Bad request - validation error")
            print(response.json())  # Print validation error details
        elif response.status_code == 500:
            print("Internal Server Error")
        else:
            print(f"Error: {response.status_code}")
            print(response.content)

    except requests.exceptions.RequestException as e:
        print(f"Error: An exception occurred while making the request: {e}")

if __name__ == "__main__":
    user_id = 3  # Replace with the ID of the user you want to update
    updated_data = {
        "name": "Ayra Starr",
        
        # Add other fields as needed
    }

    update_user(user_id, updated_data)
