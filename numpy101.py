import numpy as np

a=np.array([1,2,3,4,5,6])
# print(a)
# print(type(a))
# print(a.ndim)                 # prints number of dimensions of array
# print(len(a))                 # prints length of array   
# print(a[0])
# print('\n')

b=np.array([[1,2,3],[4,5,6]])
# print(b)
# print(b[1,2])
# print(b.shape)                # returns number of elements in each dimension
# print('\n')

# c=a.reshape(2,3)              # change number of elements in each dimension
# print(c)

# print('\n')
# d=np.array([[1,2,3],[4,5,6]])
# e=a.reshape(3,2)
# print(e)

# f=np.ones([3,4])              # returns a new array of given shape and data type, where the element's value is set to 1
# print(f,'\n')

# g=np.zeros([3,4])             # returns a new array of given shape and data type, where the element's value is set to 0
# print(g,'\n')

# h=np.arange(5)                # creates and array from 0 to 4
# print(h,'\n')

# i=np.full([2,3],66)           # creates an array with specified element
# print(i,'\n')

# j=np.eye(3)
# print(j,'\n')

# k=np.random.random((4,5))
# print(k,'\n')

##### Pattern #####
# l=np.ones((5,5))
# m=np.zeros((3,3))
# l[1:4,1:4]=m
# l[2,2]=9
# print(l,'\n')

# b=a                       # this does not copy a in b 
# b[0]=100
# print(a[0])

# b=a.copy()
# b[0]=100
# print(a[0])

# n=np.array([1,2,3])
# o=np.array([4,5,6])
# print(np.add(n,o))                   # a+b
# print(np.subtract(n,o))              # a-b
# print(np.multiply(n,o))              # a*b
# print(np.divide(n,o))                # a/b

# print(np.sum(b))
# print(np.sum(b,axis=0))
# print(np.sum(b,axis=1))

