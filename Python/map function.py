def add(n):
    return n+n

num=(1,2,3,4,5)
res=map(add,num)
print(list(res))

#modify string using map()

l=['sat','sun','mon','tue']

test=list(map(list,l))
print(test)

#if statemennt with map()

def double_even(n):
    if n%2==0:
        return n*2
    else:
        return n

numbers=[11,24,45,35,78]

res=list(map(double_even,numbers))

print(res)

