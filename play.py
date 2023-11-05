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
song_uri = '4cOdK2wGLETKBW3PvgPWqT'
top_50_global_uri = '37i9dQZEVXbMDoHDwVN2tF'
t = '6U6mg5goDZbyTYu704iIcv'

# pauses music if number != -1, plays music if number = 1
def pause():
    sp.pause_playback() 
    
def play():
     sp.start_playback()
    
# plays the playlist from the uirs array   
def play_playlist():
    sp.start_playback(context_uri='spotify:playlist:'+top_50_global_uri)

song_uri = '4cOdK2wGLETKBW3PvgPWqT'
t = '6U6mg5goDZbyTYu704iIcv'

def play_song():
    sp.start_playback(uris=['spotify:track:' + song_uri])


