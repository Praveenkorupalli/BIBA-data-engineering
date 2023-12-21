#for loop
n=5
for i in range(0,n):
    print(i)

l=["s","for","hexaware"]
for i in l:
    print(i)

for letter in 'HexwareforHexware': 
    if letter == 'e' or letter == 's': 
        continue
    print('Current Letter :', letter)
    
#else with for loop#
list=["hexaware","for","hexaware"]
for i in range(len(list)):
    print(list[i])
else:
    print('in else block')
        
print(len(list))
