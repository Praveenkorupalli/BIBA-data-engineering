#sum of all the numbers in a list

def sum(numbers):
    total=0
    for x in numbers:
        total+=x
    return total

print(sum((8,2,3,0,7)))

#program to reverse a string

def string_reverse(itr):
    return itr[::-1]
str1='hexaware'
print('orignal string:',str1)
print('reversed string:',string_reverse('hexaware'))

#factorial
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

#unique list printing
def unique_list(l):
    x=[]
    for a in l:
        if a not in x:
            x.append(a)
    return x
print(unique_list([1,2,3,4,5,2,4,7]))


      