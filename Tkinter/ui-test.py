from tkinter import *

window = Tk()

def kg_to_convert():
    kg_to_grams()
    kg_to_pounds()
    kg_to_ounces()

def kg_to_grams():
    grams = float(e1Value.get())*1000
    t1.delete(index1='1.0', index2='end')
    t1.insert(END, grams)

def kg_to_pounds():
    pounds = float(e1Value.get())*2.20462
    t2.delete(index1='1.0', index2='end')
    t2.insert(END, pounds)

def kg_to_ounces():
    ounces = float(e1Value.get())*35.2739199982575
    t3.delete(index1='1.0', index2='end')
    t3.insert(END, ounces)

l1 = Label(window, text='Kg')
l1.grid(row=0, column=0)

b1 = Button(window, text='Convert', command=kg_to_convert)
b1.grid(row=0, column=2)

e1Value = StringVar()
e1 = Entry(window, textvariable=e1Value)
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=0)

t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=1)

t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=2)

window.mainloop()