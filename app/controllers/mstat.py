from datetime import *
from master import *

class Mstat:

    mystat = []
    
    def add_stat(self, left, right, qanswer):

        row = {
                'uid':str(Master().get_user_id()),
                'left':left,
                'right':right,
                'qstart':self.get_time(),
                'qtime':'',
                'qanswer':qanswer,
                'uanswer':'',
                'correct':'',
                'allstat':''
            }
        self.mystat.append(row)
        # print(self.mystat)

    def update_stat(self, list):
        self.mystat[-1]['qtime'] = self.get_answer_time(self.mystat[-1]['qstart'], self.get_time())
        self.mystat[-1]['uanswer'] = list
        self.mystat[-1]['correct'] = self.check_answer(list, self.mystat[-1]['qanswer'])
        self.mystat[-1]['allstat'] = self.get_all_time_stat()
        # print(self.mystat)

    def check_answer(self, user_answer, correct_answer):
        if(user_answer == correct_answer):
            return 1
        return 0

    def get_answer_time(self, start, stop):

        difference = (datetime.fromisoformat(stop) - datetime.fromisoformat(start))
        difference = difference.total_seconds()
        return difference

    def get_all_time_stat(self):
        allanswers = len(self.mystat)
        totaltime = 0
        if (len(self.mystat)>1):
            for time in self.mystat:
                totaltime += time['qtime']
                
            average = int(totaltime / allanswers)
        else:
            average = 0

        print(f"\nYour average answer time is: {average} seconds")
        return average

    def get_time(self):
        now = datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")