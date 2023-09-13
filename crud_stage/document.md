

# CRUD Operation API Documentation

 Introduction

Welcome to the `Crud_OPERATION` API documentation. This API is designed to perform CRUD (Create, Read, Update, Delete) operations on a collection of users. It allows you to manage user records efficiently.

 Table of Contents

- Prerequisites
- Getting Started
  - Installation
  - Configuration
- Authentication
- Endpoints
  - Create a User
  - Retrieve User Details
  - Update User Information
  - Delete User
- Examples Usage
- Error Handling
- Contact Information
- FAQ
- Conclusion

* Prerequisites

Before using the `Crud_OPERATION` API, ensure the following prerequisites are met:

- Python 3.7 or higher
- Django 3.2 or higher
- Django Rest Framework
- Database setup

* Getting Started

### Installation

To install and run the `Crud_OPERATION` API locally, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/Decodeine/CRUD_STAGE/.git
   ```

2. Change directory:

   ```shell
   cd Crud_OPERATION
   ```

3. Create and activate a virtual environment (recommended):

   ```shell
   python3 -m venv venv
   source venv/bin/activate
 

4. Install dependencies:

   ```shell
   pip install -r requirements.txt
   ```

### Configuration

To configure the API, set the necessary environment variables, database settings, and API keys. Refer to the project Readme documentation for detailed configuration instructions.


## Endpoints

The following endpoints are available in the `Crud_OPERATION` API:
 
1. Create a User

- **Description**: Create a new user.
- **HTTP Method**: POST
- **URL**: ` ‘https://hngxstage2.onrender.com/api’


#### Request

- **Parameters**: None
- **Sample usage**:
import requests
import json

# Define the API endpoint 
url = 'https://hngxstage2.onrender.com/api'  

# Define the data for the new user in the format expected by your API
data = {
    "name": "Janet",
}

# Send a POST request with JSON data and the appropriate headers
headers = {'Content-Type': 'application/json'}

try:
    response = requests.post(url, data=json.dumps(data), headers=headers)

    # Check the response
    if response.status_code == 201:
        print("User created successfully")
        print(response.content)
    else:
        print("Error:", response.status_code)
        print(response.content)
except requests.exceptions.RequestException as e:
    print("Error making the request:", str(e))

  ```

#### Response

- **Status Codes**: 201 Created, 400 Bad Request, 401 Unauthorized
- **Response Format**: JSON
- **Example Response**:

  ```json
  {
    "id": 1,
    "name": "John Doe"
  }
  ```


2.Retrieve User Details

- **Description**: Retrieve user details by ID or name.
- **HTTP Method**: GET
- **URL**: ‘https://hngxstage2.onrender.com/api/<str:pk_or_name>/’


#### Request

- **Parameters**:
  - `pk_or_name`: User ID or name

- **Example URL**: ` https://hngxstage2.onrender.com/api/1/` or ‘https://hngxstage2.onrender.com/api /johndoe/`.

**Sample Usage**
import requests

def fetch_person_details(person_id):
    # Define the API endpoint URL with only the person ID
    url = f'https://hngxstage2.onrender.com/api/{person_id}/'

    try:
        # Send a GET request to the API
        response = requests.get(url)

        # Check if the request was successful (HTTP status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            person_data = response.json()

            # Display the person details
            print("Person Details:")
            print(f"Name: {person_data.get('name', 'N/A')}")
            print(f"Age: {person_data.get('age', 'N/A')}")
            print(f"Sex: {person_data.get('Sex', 'N/A')}")  # 'Sex' with capital 'S'

        else:
            print(f"Error: Failed to fetch person details (HTTP Status Code {response.status_code})")

    except requests.exceptions.RequestException as e:
        print(f"Error: An exception occurred while making the request: {e}")

if __name__ == "__main__":
    person_id = 4 # Replace with the ID of the person you want to fetch
    fetch_person_details(person_id)
...............

#### Response

- **Status Codes**: 200 OK, 404 Not Found
- **Response Format**: JSON
- **Example Response**:

  ```json
  {
    "id": 1,
    "name": "John Doe",

  }
  ```

3.Update User Information

- **Description**: Update user details by ID or name.
- **HTTP Method**: PUT
- **URL**: ` https://hngxstage2.onrender.com/api /<str:pk_or_name>/`
 **Sample Usage**
 import requests
import json

# Define the base URL of your API
base_url ='https://hngxstage2.onrender.com/api/'
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
    user_id = 4  # Replace with the ID of the user you want to update
    updated_data = {
        "name": "Nana whemzy",
        
        # Add other fields as needed
    }

    update_user(user_id, updated_data)
................


#### Request

- **Parameters**:
  - `pk_or_name`: User ID or name

- **Request Body**:

  ```json
  {
    "name": "Updated Name",
    // Updated user data
  }
  ```

#### Response

- **Status Codes**: 200 OK, 400 Bad Request, 404 Not Found
- **Response Format**: JSON
- **Example Response**:

  ```json
  
{ User details updated succesfully }
  ```

4. Delete User

- **Description**: Delete a user by ID or name.
- **HTTP Method**: DELETE
- **URL**: ‘https://hngxstage2.onrender.com/api /<str:pk_or_name>/`


#### Request

- **Parameters**:
  - `pk_or_name`: User ID or name

  **Sample Usage**
  import requests

# Define the base URL of your API
base_url = 'https://hngxstage2.onrender.com/api/'

# Function to delete a user by user_id
def delete_user(user_id):
    # Define the endpoint for deleting a user
    endpoint = f'{base_url}{user_id}/'

    try:
        # Send a DELETE request to delete the user
        response = requests.delete(endpoint)

        # Check the response
        if response.status_code == 204:
            print("User deleted successfully")
        elif response.status_code == 404:
            print("User not found")
        elif response.status_code == 500:
            print("Internal Server Error")
        else:
            print(f"Error: {response.status_code}")
            print(response.content)

    except requests.exceptions.RequestException as e:
        print(f"Error: An exception occurred while making the request: {e}")

if __name__ == "__main__":
    user_id = 5

    # Call the delete_user function to delete the user
    delete_user(user_id)
..........................

#### Response

- **Status Codes**: 204 No Content, 404 Not Found

..............

## Error Handling
Possible Error Codes and Meanings

Here's a list of possible HTTP status codes you may encounter in your Crud_OPERATION API and their meanings:
•	200 OK: Successful request.
•	201 Created: Resource successfully created.
•	204 No Content: Successful request with no response body (e.g., successful DELETE request).
•	400 Bad Request: Client sent an invalid request (e.g., missing or invalid parameters).
•	401 Unauthorized: Authentication required or invalid credentials.
•	403 Forbidden: Authenticated user doesn't have permission to access the resource.
•	404 Not Found: Resource not found.
•	405 Method Not Allowed: The requested HTTP method is not allowed on this endpoint.
•	500 Internal Server Error: Unexpected server error.






## Contact Information


## FAQ

## Conclusion

Thank you for using the `Crud_OPERATION` API. Your feedback and contributions are highly appreciated.

---


