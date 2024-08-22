from playsound import playsound as ps #for the sounds
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from PIL import ImageTk, Image #for loading images
import threading # so multiple sounds can play at the same time

import os #so i can loop through repository sounds folder

#If adding a new sound make image icon and sound named the same thing
# the folder goes alphabetically 

soundboard = tk.Tk()
soundboard.geometry('700x500')

#importing sounds using os.walk()
for item in os.walk('.\\sounds', topdown=True):
    sounds = item[2]
    
#importing images using os.walk() and tkinter PhotoImage
for item in os.walk('.\\images', topdown=True):
    images = item[2]

#load and resize all images
imgSpecs = {}
for image in images:
    a = images.index(image)
    tempimg = Image.open('images/'+str(image))
    resized = tempimg.resize((100,100), Image.LANCZOS)
    final = ImageTk.PhotoImage(resized, master=soundboard)
    
    imgSpecs.update({'img'+str(a) : final})
    
buttonSounds = {}
for sound in sounds:
    buttonSounds.update({'button'+str(sounds.index(sound)) : 'sounds\\'+ sound})
    
def play(path): #function called by all buttons
    ps(path)

#pass location of the sound to play() using args
def threadplay(button):
    path = buttonSounds[button]
    threadsound = threading.Thread(target=play, args=(path,)) # args has to be a tuple
    threadsound.start()
    
#set up soundboard frame
boardframe = tk.Frame(master=soundboard)
boardframe.pack(side='top')

#col, row, specs for width of board
currRow = 0
currCol = 1
stopat = 4

for sound in sounds:
    i = sounds.index(sound)
    
    newbutton = tk.Button(
        boardframe,
        image = imgSpecs['img'+str(i)],
        relief='raised',
        command = lambda sound=sound : threadplay('button'+str(sounds.index(sound))) #need the lambda 
                                                                                    #i doesn't work here for some reason
    )
    
    # putting buttons in the frame 
    newbutton.grid(row=currRow, column=currCol, padx=0.5, pady=1)
    if currCol == stopat:
        currRow += 1
        currCol = 0
    
    currCol += 1

soundboard.mainloop()