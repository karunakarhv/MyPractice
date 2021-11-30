import os
import sys
from tkinter import *
import pygame

APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))
root = Tk()
root.title('Karun Music Player')
iconPath = os.path.join(APP_FOLDER, 'music.ico')
root.iconbitmap(iconPath)
root.geometry('500x400')


pygame.mixer.init()

def play():
    mp3Path = os.path.join(APP_FOLDER, 'test.mp3')
    pygame.mixer.music.load(mp3Path)
    pygame.mixer.music.play(loops=0)

playButton = Button(root, text='Play Song', command=play)
playButton.pack(pady=20)

def stop():
    pygame.mixer.music.stop()

stopButton = Button(root, text='Stop', command=stop)
stopButton.pack(pady=20)

root.mainloop()