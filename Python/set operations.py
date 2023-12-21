people={"jay",'ram','yesh'}
vampires={'steffin','damon'}
dracula={'khaleesi','dragons'}

#union

population=people.union(vampires)
print('set after union:', population)

#union using | operator
population=people|dracula
print('set after using | operator in union:',population)

#intersection

set1=set()
set2=set()

for i in range(1,5):
    set1.add(i)
    
for j in range(10):
    set2.add(j)
    
print('\nset1:',set1)
print('set2:',set2)

set3=set1.intersection(set2)
print('set after intersection:',set3)

#intersection using & operator

set3=set1&set2
print('set after using & operator:',set3)

#difference
set1=set()
set2=set()

for i in range(5):
    set1.add(i)
    
for j in range(5,10):
    set2.add(j)
    
print('\nset1:',set1)
print('set2:',set2)

#difference of 2 sets using difference function
set3=set1.difference(set2)
print('set difference:',set3)

#difefrence using '-' operator
set3=set1-set2
print('difference set:',set3)

set3.clear()
print('\n',set3)

#disjoint sets

s3=set1.isdisjoint(set2)
print('disjoint sets:',s3)

#subset

s4=set1.issubset(set2)
print('subset:',s4)

#superset

s5=set1.issuperset(set2)
print('is it superset:',s5)

#symmetric difference
s6=set1.symmetric_difference(set2)
print('symmetric difference:',s6)

#symmetric difference update
s7=set1.symmetric_difference_update(set2)
print('symmetric difefrence update:',s7)