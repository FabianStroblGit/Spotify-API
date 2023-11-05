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





# How to get Client_id and Client_secret
First have have to Create a Spotify Developer account.

Go to https://developer.spotify.com/ and log in with your spotify account. 

Click an your account in the top right corner and and go to Dashboard.

<img width="269" alt="Bildschirmfoto 2023-11-05 um 11 39 00" src="https://github.com/FabianStroblGit/Spotify-API/assets/117905035/323f055f-16f1-4ff4-97bf-e4e73ef69297">

Create an App

<img width="1439" alt="Bildschirmfoto 2023-11-05 um 11 43 19" src="https://github.com/FabianStroblGit/Spotify-API/assets/117905035/38d7caed-31c3-415e-829f-ccf8e946e826">

Then click on Settings in the top right corner, there are your client_id and client_secret

<img width="1420" alt="Bildschirmfoto 2023-11-05 um 11 45 40" src="https://github.com/FabianStroblGit/Spotify-API/assets/117905035/8dbcc6ba-6d94-40c7-8360-e74d857de94d">

