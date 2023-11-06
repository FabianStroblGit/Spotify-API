import requests
import base64

# create the token needed for atuhentication 
def get_auth_header(client_id, client_secret):
    
    # store and convert the id and secret 
    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

    # send the convertet data and recieve the token
    url = "https://accounts.spotify.com/api/token"
    headers = {"Authorization": f"Basic {auth_base64}"}
    data = {"grant_type": "client_credentials"}
    result = requests.post(url, headers=headers, data=data)

    # check the respone code and return the authentication header 
    if result.status_code == 200:
        token = result.json().get("access_token")
        return {"Authorization": f"Bearer {token}"}
    else:
        exit(["authentication error"])
    
# search for a song or playlist
def search_for_item(item_name, item_type, headers):
    
    url = "https://api.spotify.com/v1/search"
    query = f"?q={item_name}&type={item_type}&limit=1"
    query_url = url + query
    result = requests.get(query_url, headers=headers)

    # code 200 means the response has succeeded 
    if result.status_code == 200:
        json_result = result.json()
        
        # return the id of the song or playlist and print what is played
        if item_type == "track":
            name = json_result["tracks"]["items"][0]["name"]
            artist = json_result["tracks"]["items"][0]["artists"][0]["name"]
            print(f"Playing the song {name} by {artist}")
            return json_result["tracks"]["items"][0]["id"]
        elif item_type == "playlist":
            name = json_result["playlists"]["items"][0]["name"]
            print(f"Playing the playlist {name}")
            return json_result["playlists"]["items"][0]["id"]
    else:
        print(f"Request failed with status code: {result.status_code}")
