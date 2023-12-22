#1.Explain Python Module with examples
#a.Import module in Python
#Renaming the Python module

#imports my_module
import my_module
my_module.greeting('Praveen')

#created calculator module which performs arithemtic operations
import calculator
print(calculator.add(5,10))
print(calculator.subtract(20,10))
print(calculator.multiply(3,6))
print(calculator.division(25,5))

#renaming the module

import calculator as calc
print(calc.add(4,9))
print(calc.subtract(4,8))


#import predefined module

import math
print(math.sqrt(25))
print(math.factorial(9))

from math import sqrt,factorial
print(sqrt(20))
print(factorial(10))

#renaming the modules
import math as mat
print(mat.sqrt(4))
print(mat.factorial(10))
print(mat.sqrt(15))
print(mat.pi)
print(mat.degrees(50))
print(mat.radians(50))
print(mat.sin(15))
print(mat.cos(24))
print(mat.tan(45.7))


import random as rand
print('\n',rand.randint(0,100))
print(rand.random())
print(rand.random()*75)

l=[1,4,5,"to","hello","python",False]

print(rand.choice(l))




