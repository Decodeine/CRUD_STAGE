import requests

def fetch_person_details(person_id):
    # Define the API endpoint URL with only the person ID
    url = f'http://localhost:8000/api/{person_id}/'

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
    person_id = 1  # Replace with the ID of the person you want to fetch
    fetch_person_details(person_id)
