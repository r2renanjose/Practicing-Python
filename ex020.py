#model 1
from random import shuffle
a1 = input('First student: ')
a2 = input('Second student: ')
a3 = input('Third student: ')
a4 = input('Fourth student: ')
list = [a1, a2, a3, a4]
shuffle(list)
print('The order of presentation will be as follows: ')
print(list)

#model 2
'''import random
a1 = input('First student: ')
a2 = input('Second student: ')
a3 = input('Third student ')
a4 = input('Fourth student ')
list = [a1, a2, a3, a4]
random.shuffle(list)
print('The order of presentation will be as follows: ')
print(list)'''
