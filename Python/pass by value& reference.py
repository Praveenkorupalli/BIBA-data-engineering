def myfun(x):
    x[0]=20
    
lst=[11,12,13,14,15]
myfun(lst)
print(lst)


#pass by reference
def f1(x):
    x=[20,30,40]

list=[1,2,3,4,5,6]
f1(list)
print(list)

#swap numbers by reference
def  swap(x,y):
    temp=x
    x=y
    y=temp
x=2
y=3
swap(x,y)
print(x)
print(y)