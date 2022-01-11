#model 1
from random import choice
a1 = input('Enter the first name: ')
a2 = input('Enter the second name: ')
a3 = input('Enter the third name: ')
a4 = input('Enter the fourth name: ')
list = [a1, a2, a3, a4]
choice = choice(list)
print('The chosen student was {}'.format(choice))

#model 2
'''import random
a1 = input('Enter the first name: ')
a2 = input('Enter the second name: ')
a3 = input('Enter the third name: ')
a4 = input('Enter the fourth name: ')
list = [a1, a2, a3, a4]
choice = random.choice(list)
print('The chosen student was {}'.format(choice))'''

