import math
from decimal import Decimal as D

circle_area = []

for i in range(1,31):
   print(math.pi*i**2)
   circle_area.append(i)

circle = []

for i in range(1,31):
    circle = math.pi * i**2
    print(circle)

circles = {}

for i in range(1,31):
    circles[i] = math.pi * i**2
    print(circles)

#DECIMALS!!
#This exercise is very interesting because is related to operations with float numbers and decimals

a = D('1.4').as_integer_ratio()

print(a)

D(0.1) * D(3) - D(0.3)

D(3.14)

D(math.pi) 

str4 = str('This too\nis a multiline one\nbuilt with triple double-quotes.')

#s = "This is Unic0de"
#>>> encoded_s = s.encode('ASCII')
>>> encoded_s
b'This is Unic0de'
>>> type(encoded_s)
<class 'bytes'>
>>> s = "This is Uníc0de"
>>> encoded_s = s.encode('utf-8')

