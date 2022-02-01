import uuid
from master import *
from question import *


class Start(Master):

    def __init__(self):

        if 'user_id' not in globals():
            self.set_user_id()
            
        Question()

Start()