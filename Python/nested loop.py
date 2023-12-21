for i in range(0,5):
    for j in range(0,5):
        print(i,j,end=' ')
    print('')
    
for i in range(0,5):
    for j in range(0,5):
        print(j,end=' ')
    print('')
    

for x in range(3):
    for y in range(1,10):
        print(y,end=' ')
    print(" ")

    
rows=int(input('enter no.of rows:'))
columns=int(input('enter no.of columns'))
symbol=input('enter a symbol:')
for x in range (rows):
    for y in range(columns):
        print(symbol,end=' ')
    print()