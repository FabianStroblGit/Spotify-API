import spotipy
import tkinter as tk 
from spotipy.oauth2 import SpotifyOAuth
from search import search_for_item, get_auth_header


# change those to your id and secret
CLIENT_ID = '<your_client_id>'
CLIENT_SECRET = '<your_client_secret>'

# feel free to change those; playlist is top 50 global
default_song_id = '4cOdK2wGLETKBW3PvgPWqT'
defualt_playlist_id = '37i9dQZEVXbMDoHDwVN2tF'

# initializes an instanze of SpotifyOAuth to play and pause music 
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri='http://localhost:8080/',
                                               scope='user-modify-playback-state'))

# plays the given song, when no song is given plays the dafault song
def play_song(id):
    to_play = id if id != "" else default_song_id
    sp.start_playback(uris=['spotify:track:' + to_play])

# plays the given playlist, when no playlist is given plays the dafault playlist
def play_playlist(id):
    to_play = id if id != "" else defualt_playlist_id
    sp.start_playback(context_uri='spotify:playlist:' + to_play)

# takes the input from the first input field and searches the song
def search_for_song_with_input():
    song_name = input_field.get()
    play_song(search_for_item(song_name,'track',header))

# takes the input from the second input field and searches the playlist
def search_for_playlist_with_input():
    playlist_name = input_field2.get()
    play_playlist(search_for_item(playlist_name,'playlist',header))

# set window title and size
window = tk.Tk()
window.title("Spotify API")
window.geometry("700x700")

# get the authentication header
header = get_auth_header(CLIENT_ID,CLIENT_SECRET)

# create four frames to hold the buttons
frame1 = tk.Frame(window)
frame1.pack(side=tk.TOP, padx=10, pady=10, fill=tk.BOTH, expand=True)

frame2 = tk.Frame(window)
frame2.pack(side=tk.TOP, padx=10, pady=10, fill=tk.BOTH, expand=True)

frame3 = tk.Frame(window)
frame3.pack(side=tk.TOP, padx=10, pady=10, fill=tk.BOTH, expand=True)

frame4 = tk.Frame(window)
frame4.pack(side=tk.TOP, padx=10, pady=10, fill=tk.BOTH, expand=True)


# create the input fields 
input_field = tk.Entry(frame3, font=("Arial", 20))
input_field.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

input_field2 = tk.Entry(frame4, font=("Arial", 20))
input_field2.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)


# create the buttons and add them to the frames
button1 = tk.Button(frame1, text="Play", font=("Arial", 20), command=lambda: sp.start_playback())
button1.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

button2 = tk.Button(frame2, text="Play a song", font=("Arial", 20), command=lambda: play_song(""))
button2.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

button3 = tk.Button(frame2, text="Top 50 Global", font=("Arial", 20), command=lambda: play_playlist(""))
button3.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

button4 = tk.Button(frame1, text="Pause", font=("Arial", 20), command=lambda: sp.pause_playback())
button4.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

button5 = tk.Button(frame3, text="Search for Song", font=("Arial", 20), command=search_for_song_with_input)
button5.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

button6 = tk.Button(frame4, text="Search for Playlist", font=("Arial", 20), command=search_for_playlist_with_input)
button6.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)


# configure all buttons to have the same size
for button in [button1, button2, button3, button4, button5, button6]:
    button.configure(width=20, height=5)

window.mainloop()


