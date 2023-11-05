import tkinter as tk 
import tkinter as tk
import play 


window = tk.Tk()
window.geometry("900x450") # set window resolution 

# create two frames to hold the buttons
frame1 = tk.Frame(window)
frame1.pack(side=tk.TOP, padx=10, pady=10, fill=tk.BOTH, expand=True)

frame2 = tk.Frame(window)
frame2.pack(side=tk.TOP, padx=10, pady=10, fill=tk.BOTH, expand=True)

# create the buttons and add them to the frames
button1 = tk.Button(frame1, text="Play", font=("Arial", 20), command=lambda: play.play())
button1.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

# uris[0]
button2 = tk.Button(frame1, text="Play a song", font=("Arial", 20), command=lambda: play.play_song())
button2.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

# uris[1]
button3 = tk.Button(frame1, text="Top 50 Global", font=("Arial", 20), command=lambda: play.play_playlist())
button3.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

button4 = tk.Button(frame2, text="Pause", font=("Arial", 20), command=lambda: play.pause())
button4.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

# uris[2]
button5 = tk.Button(frame2, text="Study", font=("Arial", 20), command=lambda: play.pause())
button5.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

# uris[3]
button6 = tk.Button(frame2, text="Sound", font=("Arial", 20), command=lambda: play.pause())
button6.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)


# configure all buttons to have the same size
for button in [button1, button2, button3, button4, button5, button6]:
    button.configure(width=20, height=5)

window.mainloop()


