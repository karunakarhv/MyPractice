from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title('Learn to code')
window.iconbitmap('myicon.ico')

my_img = ImageTk.PhotoImage(Image.open('bluebird.jpg'))
my_label = Label(image=my_img)
my_label.pack()


button_quit = Button(window, text='Exit Program', command=window.quit)
button_quit.pack()

window.mainloop()