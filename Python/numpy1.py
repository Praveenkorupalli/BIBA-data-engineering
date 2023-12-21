import numpy as np

arr=np.array([[1,2,3],
              [4,5,6]])
print("array type:",type(arr))

print("no.of dimensions:",arr.ndim)

print("shape of array:",arr.shape)

print("size of array:",arr.size)

print("array stores elements of type:",arr.dtype)


a=np.array([[1,2,4],[4,6,5,]],dtype='float')
print(a)

b=np.array((1,3,8))
print('\n array created using tuple:',b)

c = np.zeros((3, 4)) 
print ("An array initialized with all zeros:\n", c)

d = np.full((3, 3), 6, dtype = 'complex') 
print ("An array initialized with all 6s." 
            "Array type is complex:\n", d) 

e=np.random.random((2,3))
print("random array:\n",e)

f=np.arange(0,30,5)
print('sequential array:\n',f)

g=np.linspace(0,5,10)
print('sequential array with 10 numbers between 0 and 5:\n',g)

#reshaping
arr=np.array([[1,3,4,5],[3,4,5,6],[7,8,9,0]])

newarr=arr.reshape(2,2,3)
print('originl array:\n',arr)
print('reshaped array:\n',newarr)

#flattended array

arr=np.array([[1,2,4],[4,5,6]])
newarr=arr.flatten()
print("\noriginal array:\n",arr)
print("flattened array:\n",newarr)

#numpy array indexing
#1.slicing

arr=np.array([[-1,2,0,4],
              [4, -0.5, 6, 0], 
              [2.6, 0, 7, 8], 
              [3, -7, 4, 2.0]])

temp=arr[:2, ::2]
print("\narray with first 2 rows and alternate columns:\n",temp)

#integer array indexing
temp = arr[[0, 1, 2, 3], [3, 2, 1, 0]]
print('\nelements at indices (0, 3), (1, 2), (2, 1),(3, 0):\n', temp)

#boolean array indexing
cond=arr>0
temp=arr[cond]
print ("\nElements greater than 0:\n", temp)

