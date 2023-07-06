from tkinter import *

class BaseApp(Tk):
    def __init__(self):
        super().__init__()
        
        self.iconbitmap('logoicon.ico')
        self.add_exit_shortcut()

    def add_exit_shortcut(self):
        self.bind('<Escape>', lambda e: self.destroy())

    def run(self):
        self.mainloop()
