from datetime import *
from master import *

class mstat:

    mystat = []
    
    def add_stat(self, left, right, qanswer):

        row = {
                'uid':str(master().get_user_id()),
                'left':left,
                'right':right,
                'qstart':self.get_time(),
                'qend':'',
                'qanswer':qanswer,
                'uanswer':''
            }
        self.mystat.append(row)
        # print(self.mystat)


    def update_stat(self, list):
        self.mystat[-1]['qend'] = self.get_time()
        self.mystat[-1]['uanswer'] = list
        # print(self.mystat)

    def get_time(self):
        now = datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")