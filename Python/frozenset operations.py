#frozenset operations
a=frozenset([1,2,3,4,5])
b=frozenset([4,5,6,7,8,9])

c=a.copy()
print(c)

print(a.union(b))

print(a.intersection(b))

print(a.difference(b))

print(a.symmetric_difference(b))
