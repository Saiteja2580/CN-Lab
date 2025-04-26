import requests

def fetch_data(url):
    try:
        print(f"Sending request to {url}...")
        response = requests.get(url)

        # Print status code
        print(f"Status Code: {response.status_code}")

        # Print a preview of the data (first 300 characters)
        print("Data Preview:")
        print(response.text[:300])

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Example usage
fetch_data("https://jsonplaceholder.typicode.com/posts/1")
