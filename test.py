import requests
import json
import base64
import requests

# Set up the API endpoint and access token
endpoint = "https://api.spotify.com/v1/me/player/play"
access_token = "YOUR_ACCESS_TOKEN"

# Set up the request headers and data
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

data = {
    "uris": ["spotify:track:TRACK_ID"]
}

# Send the request to the API endpoint
response = requests.put(endpoint, headers=headers, data=json.dumps(data))

# Check the response status code
if response.status_code == 204:
    print("Song is now playing on Spotify!")
else:
    print("Failed to play song on Spotify.")

    # Set up the client ID and client secret
    client_id = "c35b4a04113d4dc6b70477e9e304d56c"
    client_secret = "ecb4e85d175546a48dc707e9ddbcd1a6"

    # Encode the client ID and client secret in base64
    client_credentials = f"{client_id}:{client_secret}"
    client_credentials_b64 = base64.b64encode(client_credentials.encode()).decode()

    # Set up the request headers and data
    headers = {
        "Authorization": f"Basic {client_credentials_b64}"
    }

    data = {
        "grant_type": "client_credentials"
    }

    # Send the request to the Spotify Accounts service
    response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)

    # Get the access token from the response
    access_token = response.json()["access_token"]
