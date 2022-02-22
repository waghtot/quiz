from tkinter import * 
import uuid
from register import *
from login import *
from question import *

class Master:

    def set_user_id(self):
        globals()['user_id'] = uuid.uuid1()
        # print(globals()['user_id'])

    def get_user_id(self):
        return globals()['user_id']

    def frame_basic(self):
        return Frame()

    def replace_with(self, data):
        self.f1.destroy()
        self.f1 = self.frame_basic()
        self.f1.grid()

        if(data == 'register'):
            Register()

        if(data == 'login'):
            Login()
        
        if(data == 'play'):
            Question()
        
        if(data == 'quit'):
            quit()
