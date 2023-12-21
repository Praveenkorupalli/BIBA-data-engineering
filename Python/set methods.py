#insertion
people={'john','snow','brad'}
print('people:',end=' ')
print(people)

people.add("daxit")
print(people)

#insertion using iterator

for i in range(1,6):
    people.add(i)
print('after adding elements:',people)

s={'g','e','e','k','s'}
t=('f','o')
l=['a','e']

#add tuple to set
s.add(t)
print('after adding tuple:',s)
#add list to set
s.update(l)
print('after updating with list:',s)

#copy
s1={1,2,3,4,5}
s2=s1.copy()
print('after copying set:',s2)

#discard
s={1,2,3,4,5,6,7}
s.discard(3)
print(s)

myset={'a',1,"pyt",2,'b',"hexaware",8}
myset.discard("hexaware")
print('after discard:',myset)

s={'h','e','x','a','w','a','r','e'}
print("\noriginal set:",s)
s.add('c')
print('after insertion:',s)

s.discard('x')
print('after discarding',s)

s.remove('e')
print('after removing',s)

print("\n popped element:",s.pop())
print('after popping:',s)

s.clear()
print("set after clearing:",s)
