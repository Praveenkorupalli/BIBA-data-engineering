
import calculator
print(calculator.add(10,2))

from math import sqrt,factorial
print(sqrt(20))
print(factorial(10))

#import all names
from math import *
print(sqrt(25))
print(factorial(7))

#locating python modules
import sys
print(sys.path)

#renaming python modules

import math as mt
print(mt.sqrt(30))
print(mt.factorial(8))


#built-in modules
import math

print(math.sqrt(15))

print(math.pi)

print(math.degrees(45))

print(math.radians(50))

print(math.sin(8))

print(math.cos(2))

print(math.tan(1.45))

print(math.factorial(5))


import random

print('\n',random.randint(0,100))

print(random.random())

print(random.random()*100)

l=[1,4,5,"hello","world",False]

print(random.choice(l))

#importing built in datetime '

import datetime
from datetime import date 
import time
print('\n',time.time())
print(date.fromtimestamp(652252))

import tempcoversion
print(tempcoversion.to_centigrade(15))

print(tempcoversion.freezing_f)

#importing particular components of module
from tempcoversion import to_fahrenheit
print(to_fahrenheit(30))

from tempcoversion import freezing_c
print(freezing_c)