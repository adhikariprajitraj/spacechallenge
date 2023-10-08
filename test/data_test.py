import os
from dotenv import load_dotenv
import requests
import json

# Replace with your actual token
api_token = os.getenv('TOKEN')

# Define the API endpoint and parameters
api_endpoint = 'https://cmr.earthdata.nasa.gov/search/collections'
params = {
    'keyword': 'EMIT',
    'token': api_token,
}

# Send a GET request to the API
response = requests.get(api_endpoint, params=params)

# Check for a valid response
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Print the data or process it further
    print(json.dumps(data, indent=4))
else:
    print(f'Failed to retrieve data: {response.status_code}')





