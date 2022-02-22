import uuid
from master import *
from question import *
from welcome import *


class Start(Master):

    def __init__(self):
        if 'user_id' not in globals():
            # print('global user_id doesn\'t exists')
            self.set_user_id()

        Welcome()
# print(globals()['user_id'])        
        # Question()

# Start()