# CRUD_STAGE
HNGx Stage 2
crud_operation
Overview:
The "crud_operation" is a flexible Django-based web application designed to facilitate Create, Read, Update, and Delete (CRUD) operations on various data entities. It serves as a robust foundation for building web applications that require efficient management of structured data.
Key Features:
1.	CRUD Functionality: The core purpose of this project is to provide a comprehensive set of tools for performing CRUD operations on data entities. Whether you're managing user profiles, or any other structured data, "crud_operation" simplifies the process.
2.	Extensible Architecture: Built on the Django framework, the project follows best practices for modular and maintainable code. You can easily extend and customize it to suit your specific data models and business requirements.
3.	RESTful API: "crud_operation" includes a RESTful API that enables seamless integration with other applications or services. 
4.	User Authentication: The project includes user authentication features, ensuring that data access and management are secure. You can easily configure and customize authentication methods to suit your needs.
5.	Database Flexibility: It supports various database backends, including PostgreSQL, MySQL, SQLite, and more, giving you the flexibility to choose the database that best suits your project's needs.
6.	Deployment-Ready: The project is designed with deployment in mind. You can easily deploy it to a variety of hosting platforms, making it suitable for both small-scale projects and enterprise-level applications.
7.	Community Support: The Django community is vast and active, providing a wealth of resources, plugins, and extensions that can be integrated with your project as needed.

Use Cases:

•	Content Management Systems (CMS)
•	Customer Relationship Management (CRM) tools
•	Inventory and Product Management Systems
•	User Profile Management
•	Blogging Platforms
•	and much more...
 
Installation
Before you can start using the "crud_operation" project, you'll need to ensure that your system meets the necessary prerequisites and follow the installation steps outlined below.
Prerequisites
Before you begin, make sure you have the following prerequisites installed on your system:
•	Python: The project is developed using Python. You'll need Python 3.7 or higher. You can download Python from the official Python website.

•	Django: This project is built on the Django web framework. You can install Django using pip, Python's package manager, with the following command:
pip install Django
pip install Django 
•	Database: You'll need a database backend to store your data. Django supports various databases, including PostgreSQL, MySQL, SQLite, and more. Choose and install a database that suits your requirements.

•	Virtual Environment (Optional, but Recommended): It's a good practice to create a virtual environment for your project to isolate its dependencies. You can create a virtual environment using Python's venv module:

python -m venv venv

Activate the virtual environment:
•	On Windows:
venv\Scripts\activate

•	On macOS and Linux:
source venv/bin/activate
Installation Steps
Follow these steps to set up and run the "crud_operation" project:
1.	Clone the Repository: Start by cloning this repository to your local machine using Git:
    git clone https://github.com/Decodeine/CRUD_STAGE.git

2.	Navigate to the Project Directory: Change your current directory to the project's root folder:
    cd Crud_OPERATION

3.	Create and Activate a Virtual Environment (Optional): If you opted to use a virtual environment, create and activate it as described in the prerequisites section above.

4.	Install Dependencies: Use pip to install the project's dependencies from the requirements.txt file:
              pip install -r requirements.txt
5.	Configure Database: Set up your database configuration in the project's settings.py file. Update the database engine, name, user, password, and other relevant settings to match your database setup.

6.	Apply Migrations: Run the following commands to apply database migrations and create the necessary database tables:
       python manage.py makemigrations
       python manage.py migrate

7.	Start the Development Server: Launch the Django development server to run the project locally:
    python manage.py runserver

8.	Access the Application: Open your web browser and navigate to http://127.0.0.1:8000/ to access the project. 

API Usage (Using Django Scripts or Tests)
The "Crud_OPERATION" project provides a set of API endpoints to perform CRUD (Create, Read, Update, Delete) operations on "Person" records within your Django application. You can interact with these API endpoints by writing Django scripts or tests. Below, you'll find examples and instructions on how to use these endpoints programmatically within your Django environment.
1. Create a Person
To create a new "Person" record, use the following example:
           import requests
import json

# Define the API endpoint 
url = 'https://hngxstage2.onrender.com/api'  

# Define the data for the new user in the format expected by your API
data = {
    "name": "Lokosa",
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


2. Retrieve a Person
To retrieve details of a specific "Person" record by ID or name, use the following example:
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


3. Update a Person
To update an existing "Person" record by ID or name, use the following example:
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


5. Delete a Person
To delete a specific "Person" record by ID or name, use the following example:
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





