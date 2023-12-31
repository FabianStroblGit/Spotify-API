# Spotify-API
This Project showcases the basic usages of Spotify API via Python. It can be operated by a simple UI to:
- play and pause music
- play a song / playlist specified in the code
- search and play a song or a playlist 

# Getting Started
To use this for yourself, you have to change the client_id and client_secret to your own in the main.py file.
``` Python
CLIENT_ID = '<your_client_id>'
CLIENT_SECRET = '<your_client_secret>'
```
If you dont know how to get those, [here](#how-to-get-client_id-and-client_secret) is an explenation.


# How it works
- An instanze of SpotifyOAuth is created using your Spotify client_id and client_secret.(More on this [later](#use-it-yourself))
```Python
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri='http://localhost:8080/',
                                               scope='user-modify-playback-state'))
```
- An authentication header is generated in search.py to be used later to search for a song or playlist.

- The UI is created using tkinter 
<img width="812" alt="image" src="https://github.com/FabianStroblGit/Spotify-API/assets/117905035/99d2dc28-192e-46bc-8299-c2cd7707dd62">


- pressing 'Play' calls the start_playback() function of the instanz of SpotifyOAuth 
```Python
sp.start_playback()
```

- pressing 'Pause' calls the pause_playback() function of the instanz of SpotifyOAuth 
```Python
sp.pause_playback()
```

- pressing 'Play a song' plays the default song set by the author. It also uses the start_playback function of SpotifyOAuth
 ```Python
default_song_id = '4cOdK2wGLETKBW3PvgPWqT'
sp.start_playback(uris=['spotify:track:' + default_song_id])
```

- pressing 'Play a playlist` plays the default playlist set by the author. It also uses the start_playback function of SpotifyOAuth
 ```Python
defualt_playlist_id = '37i9dQZEVXbMDoHDwVN2tF'
sp.start_playback(context_uri='spotify:playlist:' + defualt_playlist_id)
```

- pressing 'Search for a Song' or 'Search for a Playlist' first take the input from the text field next to the button, then searches via the Spotify search APi for the song
```Python
item_name = 'Never Gonna Give You Up'
item_type = 'song' # or 'playlist'
url = "https://api.spotify.com/v1/search"
query = f"?q={item_name}&type={item_type}&limit=1"
query_url = url + query
result = requests.get(query_url, headers=headers)
```

Then the name, id and the artist are extracted from the result. 
```Python
name = json_result["tracks"]["items"][0]["name"]
artist = json_result["tracks"]["items"][0]["artists"][0]["name"]
print(f"Playing the song {name} by {artist}")
return json_result["tracks"]["items"][0]["id"]
```

Those are then played by the start_playback() function of SpotifyOAuth
```Python
play_song(search_for_item(song_name,'track',header))
```


# Change default song or playlist
In the main.py file there are 2 variable for a default song an playlist.

``` Python
default_song_id = '4cOdK2wGLETKBW3PvgPWqT'
default_playlist_id = '37i9dQZEVXbMDoHDwVN2tF'
```
The playlist is 'Top 50 Global', you can try for yourself what the song is. 

To change those you need the song or playlist id, you can go into Spotify and choose a song or a playlist. Then right click it (or press the 3 dots) and press share -> copy songlink. The link will look like the following: 


https://open.spotify.com/intl-de/track/4cOdK2wGLETKBW3PvgPWqT?si=79c891f1078b4f48


The only important part is after the last / and before the ?, in this case '4cOdK2wGLETKBW3PvgPWqT'. Now replace the default_song_id or default_playlist_id with the new value.



# How to get Client_id and Client_secret
First have have to Create a Spotify Developer account.

Go to https://developer.spotify.com/ and log in with your spotify account. 

Click an your account in the top right corner and and go to Dashboard.

<img width="269" alt="Bildschirmfoto 2023-11-05 um 11 39 00" src="https://github.com/FabianStroblGit/Spotify-API/assets/117905035/323f055f-16f1-4ff4-97bf-e4e73ef69297">

Create an App

<img width="1439" alt="Bildschirmfoto 2023-11-05 um 11 43 19" src="https://github.com/FabianStroblGit/Spotify-API/assets/117905035/38d7caed-31c3-415e-829f-ccf8e946e826">

Then click on Settings in the top right corner, there are your client_id and client_secret

<img width="1420" alt="Bildschirmfoto 2023-11-05 um 11 45 40" src="https://github.com/FabianStroblGit/Spotify-API/assets/117905035/8dbcc6ba-6d94-40c7-8360-e74d857de94d">

