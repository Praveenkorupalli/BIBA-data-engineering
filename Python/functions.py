def fun():
    print("welcome to python")
fun()

def fun(n1,n2):
    n3=n1+n2
    print(n3)
fun(4,5)

def printsuccess():
    print('i am done')
    print('send me another task')
printsuccess()

def hello(name,age):
    print("hello"+name+"you are"+str(age)+"years old")
    
hello('beau',39)


def hello(name):
    print('hello'+name+'!')
    return name,'beau',8
print(hello('syd'))



#function with parameters

def add(num1: int, num2: int) -> int:
    """Add two numbers"""
    num3 = num1 + num2
 
    return num3
 
# Driver code
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")


