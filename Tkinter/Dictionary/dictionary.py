from tkinter import *
from tkinter import messagebox
from itertools import chain
from nltk.corpus import wordnet as wn

def meaning(myText):
    myText = myText.strip('\n')
    syn = wn.synsets(myText)
    meanList = [word.definition() for word in syn]
    if meanList:
        return meanList
    return 'Not found'

def synonyms(myText):
    myText = myText.strip('\n')
    syn = wn.synsets(myText)
    wordSet = set(chain.from_iterable([word.lemma_names() for word in syn]))
    if wordSet:
        return wordSet
    return 'Not found'

def antonyms(myText):
    antList = []
    myText = myText.strip('\n')
    syn = wn.synsets(myText)
    for word in syn:
        for ant in word.lemmas():
            if ant.antonyms():
                antList.append(ant.antonyms()[0].name())
    if antList:
        return set(antList)
    return 'Not found'

def examples(myText):
    myText = myText.strip('\n')
    syn = wn.synsets(myText)
    exampleList = [word.examples() for word in syn]
    if exampleList:
        return exampleList
    return 'Not found'

def getMeaning():
    # Delete any previous translate
    meaningText.delete(1.0, END)
    try:
        meaningWord = meaning(origText.get(1.0, END))
        if meaningWord is None:
            meaningText.insert(1.0, 'Not found')
            return
        meaningText.insert(1.0, meaningWord)

    except Exception as e:
        messagebox.showerror('Not found in dictionary!!', e)

def getSynonym():
    # Delete any previous translate
    meaningText.delete(1.0, END)
    try:
        meaning = synonyms(origText.get(1.0, END))
        if meaning is None:
            meaningText.insert(1.0, 'Not found')
            return
        meaningText.insert(1.0, meaning)
    except Exception as e:
        messagebox.showerror('Not found in dictionary!!', e)

def getAntonym():
    # Delete any previous translate
    meaningText.delete(1.0, END)
    try:
        meaning = antonyms(origText.get(1.0, END))
        if meaning is None:
            meaningText.insert(1.0, 'Not found')
            return
        meaningText.insert(1.0, meaning)
    except Exception as e:
        messagebox.showerror('Not found in dictionary!!', e)

def getExamples():
    # Delete any previous translate
    meaningText.delete(1.0, END)
    try:
        meaning = examples(origText.get(1.0, END))
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

originalTextLabel = Label(window, text="Input Word")
originalTextLabel.grid(row=0, column=0)

outputTextLabel = Label(window, text="Output")
outputTextLabel.grid(row=0, column=4)

# Text Box
origText = Text(window, height=10, width=40)
origText.grid(row=1, column=0, padx=10, pady=20, rowspan=3, columnspan=3)

meaningBtn = Button(window, text='Meaning', font=("Helvetica", 12), command=getMeaning)
meaningBtn.grid(row=5, column=1, padx=10, pady=20)

synonymsBtn = Button(window, text='Synonym', font=("Helvetica", 12), command=getSynonym)
synonymsBtn.grid(row=5, column=2, padx=10, pady=20)

antonymBtn = Button(window, text='Antonym', font=("Helvetica", 12), command=getAntonym)
antonymBtn.grid(row=5, column=3, padx=10, pady=20)

exampleBtn = Button(window, text='Examples', font=("Helvetica", 12), command=getExamples)
exampleBtn.grid(row=5, column=4, padx=10, pady=20)

meaningText = Text(window, height=10, width=40)
meaningText.grid(row=1, column=4, padx=10, pady=20, rowspan=3, columnspan=3)

clearBtn = Button(window, text='Clear', command=clear)
clearBtn.grid(row=5, column=5)


window.mainloop()