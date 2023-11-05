# Spotify-API
This project lets you pause and play spotify on a basic UI, as well as play different playlists. 

# Self use 
To use this for yourself, you have to change the client_id and client_secret to your own in the play.py file.
``` Python
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=<your_client_id>,
                                               client_secret=<your_client_secret>,
                                               redirect_uri='http://localhost:8080/',
                                               scope='user-modify-playback-state')) 
```
If you dont know how to get those values, [here](#how-to-get-client_id-and-client_secret) is an explenation.

# Use ur own playlists
First you have to get the link to the playlist. This can be done by going into Spotify, then rightclicking the playlist, clicking on share and copying the link. The result will look like the following: https://open.spotify.com/playlist/37i9dQZF1DX4jP4eebSWR9?si=9f23f9c1a8584730

The important part for this implementation ist 37i9dQZF1DX4jP4eebSWR9, so just cut the rest.

Paste this in the uris array in play.py.

```Python
uris = [
'0mFJCyKyW3nZS1GNbfMZY9', #gym
'37i9dQZEVXcBYzyq5963Jf', #mix
'2SIoGgxJQvDfNMVNaqzR9r', #lofi
'3s6gW3ERpwFncWhi4ynmjz', #study
'2Xt965bzJpBb2JMR6YyGTa'  #sound
]
```
and you can change the name accordingly in main.py

```Python
button2 = tk.Button(frame1, text=<your_playlist-name>, font=("Arial", 20), command=lambda: button_click(0))
button2.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)
```

# How to get Client_id and Client_secret
First have have to Create a Spotify Developer account.

Go to https://developer.spotify.com/ and log in with your spotify account. 

Click an your account in the top right corner and and go to Dashboard.

<img width="269" alt="Bildschirmfoto 2023-11-05 um 11 39 00" src="https://github.com/FabianStroblGit/Spotify-API/assets/117905035/323f055f-16f1-4ff4-97bf-e4e73ef69297">

Create an App

<img width="1439" alt="Bildschirmfoto 2023-11-05 um 11 43 19" src="https://github.com/FabianStroblGit/Spotify-API/assets/117905035/38d7caed-31c3-415e-829f-ccf8e946e826">

Then click on Settings in the top right corner, there are your client_id and client_secret

<img width="1420" alt="Bildschirmfoto 2023-11-05 um 11 45 40" src="https://github.com/FabianStroblGit/Spotify-API/assets/117905035/8dbcc6ba-6d94-40c7-8360-e74d857de94d">

