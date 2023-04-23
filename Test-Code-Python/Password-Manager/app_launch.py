from multiprocessing import Manager
from tkinter import *
from passwd_mgr_ui import PasswordMgrUI

class PasswordMgr(object):

    def __init__(self) -> None:
        super().__init__()

    def main():
        window = Tk()
        window.title('Password Manager')
        app = PasswordMgrUI(window)

        window.geometry('800x500+500+200') #Width x Height
        window.mainloop()

if __name__ == '__main__':
    PasswordMgr.main()
