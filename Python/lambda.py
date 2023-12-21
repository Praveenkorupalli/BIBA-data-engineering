str1 = 'HexaforHexa'
 
upper = lambda string: string.upper()
print(upper(str1))

format_numeric = lambda num: f"{num:e}" if isinstance(num, int) else f"{num:,.2f}"
 
print("Int formatting:", format_numeric(1000000))
print("float formatting:", format_numeric(999999.789541235))



is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
for item in is_even_list:
    print(item())
    
Max=lambda a,b: a if (a>b) else b
print(max(1,2))


def cube(y):
    return y*y*y
 
lambda_cube = lambda y: y*y*y
print("Using function defined with `def` keyword, cube:", cube(5))
print("Using lambda function, cube:", lambda_cube(5))

#lambda with multiple statements
List = [[2,3,4],[1, 4, 16, 64],[3, 6, 9, 12]]
 
sortList = lambda x: (sorted(i) for i in x)
secondLargest = lambda x, f : [y[len(y)-2] for y in f(x)]
res = secondLargest(List, sortList)
print(res)
