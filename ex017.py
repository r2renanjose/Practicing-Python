#model 1
'''co = float(input('Length of opposite leg: '))
ca = float(input('Length of adjacent leg: '))
hi = (co ** 2 + ca ** 2) ** (1 / 2)
print('The hypotenuse will measure: {:.2f}'.format(hi))'''

#model 2
import math
co = float(input('Length of opposite leg: '))
ca = float(input('Length of adjacent leg: '))
hi = math.hypot(co, ca)
print('The hypotenuse will measure: {:.2f}'.format(hi))

#model 3
'''from math import hypot
co = float(input('Length of opposite leg: '))
ca = float(input('Length of adjacent leg: '))
hi = hypot(co, ca)
print('The hypotenuse will measure: {:.2f}'.format(hi))'''
