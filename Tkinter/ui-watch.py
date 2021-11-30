from tkinter import *
from datetime import datetime, time
from dateutil.tz import gettz

import tkinter

window = Tk()
window.title('My Digital Clock')

text_font= ("Boulder", 45, 'bold')
background = "black"
foreground= "green"
border_width = 25

def time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S %p")
    l1.config(text = current_time)
    l1.after(1000, time)

l1 = Label(window, font=text_font, bg=background, fg=foreground, bd=border_width)
l1.pack(anchor=CENTER)

time()
window.mainloop()