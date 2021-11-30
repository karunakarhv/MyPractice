from tkinter import *

window = Tk()
window.title('My Calculator App')

entry = Entry(window, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(val):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(val))

def button_clear():
    entry.delete(0, END)

def button_add():
    first_number = entry.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_number)
    entry.delete(0, END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, END)
    if math == 'addition':
        entry.insert(0, f_num + int(second_number))
    if math == 'subtraction':
        entry.insert(0, f_num - int(second_number))
    if math == 'multiplication':
        entry.insert(0, f_num * int(second_number))
    if math == 'division':
        entry.insert(0, f_num / int(second_number))

def button_subtract():
    first_number = entry.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_number)
    entry.delete(0, END)

def button_multiply():
    first_number = entry.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_number)
    entry.delete(0, END)

def button_divide():
    first_number = entry.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_number)
    entry.delete(0, END)

button1 = Button(window, padx=40, pady=20, text='1', command=lambda :button_click(1))
button2 = Button(window, padx=40, pady=20, text='2', command=lambda :button_click(2))
button3 = Button(window, padx=40, pady=20, text='3', command=lambda :button_click(3))
button4 = Button(window, padx=40, pady=20, text='4', command=lambda :button_click(4))
button5 = Button(window, padx=40, pady=20, text='5', command=lambda :button_click(5))
button6 = Button(window, padx=40, pady=20, text='6', command=lambda :button_click(6))
button7 = Button(window, padx=40, pady=20, text='7', command=lambda :button_click(7))
button8 = Button(window, padx=40, pady=20, text='8', command=lambda :button_click(8))
button9 = Button(window, padx=40, pady=20, text='9', command=lambda :button_click(9))
button0 = Button(window, padx=40, pady=20, text='0', command=lambda :button_click(0))
button_plus = Button(window, padx=40, pady=20, text='+', command=button_add)
button_clear = Button(window, padx=79, pady=20, text='Clear', command=button_clear)
button_equal = Button(window, padx=91, pady=20, text='=', command=button_equal)


button_subtract = Button(window, padx=42, pady=20, text='-', command=button_subtract)
button_multiply = Button(window, padx=42, pady=20, text='*', command=button_multiply)
button_divide = Button(window, padx=42, pady=20, text='/', command=button_divide)

button0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_plus.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

window.mainloop()