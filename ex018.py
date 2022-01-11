#model 1
'''import math
angle = float(input('Enter the angle you want: '))
sn = math.sin(math.radians(angle))
print('The angle of {} has the SINE of {:.2f}'.format(angle, sn))
cos = math.cos(math.radians(angle))
print('The angle of {} has the COSINE of {:.2f}'.format(angle, cos))
tg = math.tan(math.radians(angle))
print('The angle of {} has the TANGENT of {:.2f}.'.format(angle, tg))'''

#model 2
from math import sin, cos, radians, tan
angle = float(input('Enter the angle you want: '))
sn = sin(radians(angle))
print('The angle of {} has the SINE of {:.2f}'.format(angle, sn))
cos = cos(radians(angle))
print('The angle of {} has the COSINE of {:.2f}'.format(angle, cos))
tg = tan(radians(angle))
print('The angle of {} has the TANGENT of {:.2f}.'.format(angle, tg))
