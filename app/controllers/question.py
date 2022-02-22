import random
from mstat import *

class Question:

    def __init__(self, left = 10, right = 10):

        left, right, linit, rinit = self.set_factor(left), self.set_factor(right), left, right
        '''
        first digit = factor lenght
        second digit defined factor as odd or even i.e. 10 = 2, 11 = 3, 20 = 14, 21 = 11 ...
        0 = even numbers
        1 = odd numbers
        '''
        if (left > right):
            a, b = right, left
        else:
            a, b = left, right

        list = []
        list = self.gen_answer(a, b)
        print(f'{a} * {b} = \n')
        print(f"a) {list['a']}, b) {list['b']}, c) {list['c']}\n")

        if(len(list)>0):
            print(list['d'])
            Mstat().add_stat(linit, rinit, list['d'])
            if(self.check_answer(list) == True):
               Question()

    def set_factor(self, number = 10):

        value = '1'
        for i in range(self.get_range(number)):
          value += '0'
        
        value = self.gen_factor(int(value), int(str(number)[1]))
        return(value)

    def gen_factor(self, number, ntype):

        left = number
        right = 10 * number
        factor = self.gen_number(left, right)
        while (factor % 2 != ntype):
            factor = self.gen_number(left, right)
        return factor

    def get_range(self, number):

        value = int(str(number)[0])
        if (value == 1):
            value = 0
        else:
            value = value - 1
        return value

    def gen_number(self, left, right):

        return random.randint(left, right)

    def gen_answer(self, left, right):

        a = int(left * right)

        if(len(str(a))>1):
            b = int((left * right) + (left / 2))
            c = int((left * right) - (left / 2))
        else:
            b = a + 1
            c = a + 2
        mylist = []
        mylist = [a, b, c]
        random.shuffle(mylist)
        answer = []
        answer={'a':mylist[0],'b':mylist[1],'c':mylist[2],'d':a}
        return answer

    def check_answer(self, list):
        
        allowed = ['a', 'b', 'c', 'q']
        answer = input(f'?: ')

        if answer not in allowed:
            self.check_answer(list)
        else:

            if(answer == 'q'):
                print(f"\nThank you for your time\nI hope you enjoyed that game.")
                return False
            else:

                Mstat().update_stat(list[answer])

                if(list['d'] == list[answer]):
                    print(f"\nYes, {list['d']} is correct answer !!!\n")
                else:
                    print(f"\nNo. Correct answer is: {list['d']}. Try again.\n")

            return True