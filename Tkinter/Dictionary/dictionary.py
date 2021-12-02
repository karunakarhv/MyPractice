from tkinter import *
from tkinter import messagebox
from PyDictionary import PyDictionary

def getMeaning():
    # Delete any previous translate
    meaningText.delete(1.0, END)
    try:
        myDictionary = PyDictionary()
        meaning = myDictionary.meaning(origText.get(1.0, END), disable_errors=True)
        if meaning is None:
            meaningText.insert(1.0, 'Not found')
            return
        meaningText.insert(1.0, meaning)

    except Exception as e:
        messagebox.showerror('Not found in dictionary!!', e)

def clear():
    origText.delete(1.0, END)
    meaningText.delete(1.0, END)

window = Tk()
window.title('Dictionary')

# Text Box
origText = Text(window, height=10, width=40)
origText.grid(row=0, column=0, padx=10, pady=20)

meaning = Button(window, text='Meaning', font=("Helvetica", 12), command=getMeaning)
meaning.grid(row=0, column=1, padx=10, pady=20)

meaningText = Text(window, height=10, width=100)
meaningText.grid(row=0, column=3, padx=10, pady=20)

clearBtn = Button(window, text='Clear', command=clear)
clearBtn.grid(row=2, column=1)


window.mainloop()