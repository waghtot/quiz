
import tkinter
from master import *

class Welcome(Master):

    def __init__(self):
        print(globals()['user_id'])
        self.f1 = self.frame_basic()
        self.f1.grid()
        Label(self.f1, text='Welcome').grid(row=0, column=0, columnspan=3, pady=10, sticky='WE')
        Button(self.f1, text="Register", command=lambda: self.replace_with('register')).grid(row=1, column=1)
        Button(self.f1, text="Login", command=lambda: self.replace_with('login')).grid(row=2, column=1)
        Button(self.f1, text="Play", command=lambda: self.replace_with('play')).grid(row=3, column=1)
        Button(self.f1, text="Quit", command=lambda: self.replace_with('quit')).grid(row=4, column=1)
