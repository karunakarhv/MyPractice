from tkinter import *

# Password Manager UI
class PasswordMgrUI(object):
    # Constructor
    def __init__(self, window):
        # Label to display instructions
        lbl_url = Label(window, text='URL', font='freesansbold')
        lbl_url.grid(row=0, column=0)

        urlText = Text(window, height=1, width=40)
        urlText.grid(row=0, column=1)

         # Label to display instructions
        lbl_username = Label(window, text='Username', font='freesansbold')
        lbl_username.grid(row=1, column=0)
        usrText = Text(window, height=1, width=40)
        usrText.grid(row=1, column=1)

        # Label to display instructions
        lbl_pwd = Label(window, text='Password', font='freesansbold')
        lbl_pwd.grid(row=2, column=0)
        pwdText = Text(window, height=1, width=40)
        pwdText.grid(row=2, column=1)

        randBtn = Button(window, text='Random Password', command=self.randPwd)
        randBtn.grid(row=3, column=0, padx=10, pady=20)

    def randPwd(self):
        pass

