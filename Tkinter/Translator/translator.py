from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox


def translateIt():
    # Delete any previous translate
    translatedText.delete(1.0, END)
    try:
        # Get Languages from the dictionary keys
        # Get From Language Key
        for key, value in languages.items():
            if (value == origCombo.get()):
                fromLangKey = key

        # Get To Language Key
        for key, value in languages.items():
            if (value == translateCombo.get()):
                toLangKey = key

        words = textblob.TextBlob(origText.get(1.0, END))
        # Translate text
        words = words.translate(from_lang=fromLangKey, to=toLangKey)

        translatedText.insert(1.0, words)

    except Exception as e:
        messagebox.showerror('Translator', e)

languages = googletrans.LANGUAGES
languageList = list(languages.values())

def clear():
    origText.delete(1.0, END)
    translatedText.delete(1.0, END)

window = Tk()
window.title('My Translator App')

# Text Box
origText = Text(window, height=10, width=40)
origText.grid(row=0, column=0, padx=10, pady=20)

translatedBtn = Button(window, text='Translate', font=("Helvetica", 24), command=translateIt)
translatedBtn.grid(row=0, column=1, padx=10, pady=20)

translatedText = Text(window, height=10, width=40)
translatedText.grid(row=0, column=2, padx=10, pady=20)

# Combo Boxes
origCombo = ttk.Combobox(window, width=50, value=languageList)
origCombo.grid(row=1, column=0)
origCombo.current(21)

translateCombo = ttk.Combobox(window, width=50, value=languageList)
translateCombo.grid(row=1, column=2)
translateCombo.current(26)

clearBtn = Button(window, text='Clear', command=clear)
clearBtn.grid(row=2, column=1)


window.mainloop()