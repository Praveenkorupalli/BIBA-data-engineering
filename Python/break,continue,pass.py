#break

for i in range(1,5):
    for j in range(2,6):
        if j%i==0:
            break
        print(i," ",j)

var = 10                   
while var > 0:              
   print ('Current variable value :', var)
   var = var -1
   if var == 5:
      break
print ("Good bye!")
    
        
#continue

for letter in 'Python':    
   if letter == 'h':
      continue
   print( 'Current Letter :', letter)

for i in range(1,11):
    if i==6:
        continue
    else:
        print(i,end=" ")
 

s="hexware"
for i in s:
    pass
def fun():
    pass
for i in s:
    if i=='w':
        print('pass executed')
        pass
    print(i)


        
