import requests

# Define the base URL of your API
base_url = 'https://hngxstage2.onrender.com/api'

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
    user_id = 1

    # Call the delete_user function to delete the user
    delete_user(user_id)
