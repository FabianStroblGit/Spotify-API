import spotipy
from spotipy.oauth2 import SpotifyOAuth

# the connection to spotfiy 
# More in the README file 
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='c35b4a04113d4dc6b70477e9e304d56c',
                                               client_secret='ecb4e85d175546a48dc707e9ddbcd1a6',
                                               redirect_uri='http://localhost:8080/',
                                               scope='user-modify-playback-state'))

# the playlists
# feel free to change them
uris = [
'0mFJCyKyW3nZS1GNbfMZY9', #gym
'37i9dQZEVXcBYzyq5963Jf', #mix
'2SIoGgxJQvDfNMVNaqzR9r', #lofi
'3s6gW3ERpwFncWhi4ynmjz', #study
'2Xt965bzJpBb2JMR6YyGTa'  #sound
]

# pauses music if number != -1, plays music if number = 1
def pause(number):
    sp.pause_playback() if number == -1 else sp.start_playback()
    
# plays the playlist from the uirs array   
def play(number):
    sp.start_playback(context_uri='spotify:playlist:'+uris[number])
