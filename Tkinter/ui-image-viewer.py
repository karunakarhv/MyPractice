from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title('Learn to code - Image Viewer')
window.iconbitmap('images/myicon.ico')

my_img = ImageTk.PhotoImage(Image.open('images/bluebird.jpg'))
my_img1 = ImageTk.PhotoImage(Image.open('images/1.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('images/2.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('images/3.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('images/4.jpg'))

image_list = [my_img, my_img1, my_img2, my_img3, my_img4]

my_label = Label(image=my_img)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(window, text='>>', command=lambda: forward(image_number+1))
    button_back = Button(window, text='<<', command=lambda:backward(image_number-1))

    if image_number == len(image_list):
        button_forward = Button(window, text='>>', state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

def backward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(window, text='>>', command=lambda: forward(image_number+1))
    button_back = Button(window, text='<<', command=lambda:backward(image_number-1))

    if image_number == 1:
        button_back = Button(window, text='<<', state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

button_back = Button(window, text='<<', command=backward, state=DISABLED)
button_forward = Button(window, text='>>', command=lambda : forward(2))
button_quit = Button(window, text='Exit Program', command=window.quit)
button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

window.mainloop()