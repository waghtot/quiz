import uuid
from master import *
from question import *


class start(master):

    def __init__(self):

        if 'user_id' not in globals():
            self.set_user_id()
            
        question()

start()