from tkinter import *
import textblob
from tkinter import messagebox


def correct():
    # Delete any previous translate
    correctedText.delete(1.0, END)
    try:
        words = textblob.TextBlob(origText.get(1.0, END))
        # Translate text
        words = words.correct()

        correctedText.insert(1.0, words)

    except Exception as e:
        messagebox.showerror('Correct It!!', e)

def suggestions():
    # Delete any previous translate
    correctedText.delete(1.0, END)
    try:
        words = textblob.Word(origText.get(1.0, END))
        # Translate text
        words = words.spellcheck()
        for word in words:
            correctedText.insert(1.0, word[0]+'\n')

    except Exception as e:
        messagebox.showerror('Correct It!!', e)

def clear():
    origText.delete(1.0, END)
    correctedText.delete(1.0, END)

window = Tk()
window.title('Spell Checker')

# Text Box
origText = Text(window, height=10, width=40)
origText.grid(row=0, column=0, padx=10, pady=20)

spellCheckBtn = Button(window, text='Correct It', font=("Helvetica", 12), command=correct)
spellCheckBtn.grid(row=0, column=1, padx=10, pady=20)

suggestionsBtn = Button(window, text='Suggestions', font=("Helvetica", 12), command=suggestions)
suggestionsBtn.grid(row=0, column=2, padx=10, pady=20)

correctedText = Text(window, height=10, width=40)
correctedText.grid(row=0, column=3, padx=10, pady=20)

clearBtn = Button(window, text='Clear', command=clear)
clearBtn.grid(row=2, column=1)


window.mainloop()