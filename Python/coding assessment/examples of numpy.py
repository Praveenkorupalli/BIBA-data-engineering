import numpy as np

a=np.array([[1,2,3],[4,5,6]])
print("type of a is:\n",type(a))

print("dimension of array:\n",a.ndim)

print("array shape:\n",a.shape)

print("array size:\n",a.size)

arr=np.array([[2,4,5,6],[4,3,2,8]],dtype='float')
print(arr)

a=np.full((3,5),7,dtype='complex')
print("array with complex numbers:\n",a)

b=np.zeros((4,5))
print("array with zeros:\n",b)

c=np.random.random((3,3))
print("random array:\n",c)

d=[[4,5,6,7],[6,9,0,7],[4,3,1,0]]

d=arr[:3, ::3]
print("\narray with first 3 rows:\n",d)

cond=d>0
temp=d[cond]
print('array with condition:\n',temp)

a=np.array([1,2,4,5,7,8])
print('after adding:\n',a+2)

print("\n after subtracting:",a-1)

print("\n after multiplication:\n",a*5)

print("\n after squaring:\n",a**2)

arr=np.array([[1,4,5,6],[9,8,3,2],[3,5,0,2]])
print("\n transposed matrix:",arr.T)

arr = np.array([[1, 5, 6], [4, 7, 2], [3, 1, 9]]) 
  

print ("\nLargest element is:", arr.max()) 
print("\nminimum element is:",arr.min())
print("\nsum of all elements:",arr.sum())

a = np.array([[1, 2], [3, 4]]) 
b = np.array([[4, 3], [2, 1]]) 
  

print ("Array sum:\n", a + b) 
print ("Array multiplication:\n", a*b) 
print ("Matrix multiplication:\n", a.dot(b))