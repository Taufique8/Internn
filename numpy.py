#numpy basic method
import numpy as np
a = np.array ([
       [2,3,4],
       [3,5,7],
       [2,4,8]], )
print("type Of The Array:",type(a))
print("Shape of The Array:",a.shape)
print("Size of the Array:",a.size)
print("Array store element of type:",a.dtype)
print('Array: \n',a)
b = np.array((2,3,4,5))
print("Array Createdd using passed tuple:\n",b)
c = np.zeros((3,2))
print(c)
d = np.full((2,3),6, dtype ='complex')
print("complex Number:\n",d)
e = np.random.random((2,2))
print("\nA random Array:\n",e)
f = np.arange(15)
print("Range:\n",f)
amber = np.array([[2,3,4,5],[3,5,7,9],[2,4,8,3]])
#print("original array\n",amber)
#fiza = amber.flatten()
#print("Flatten Array",fiza)
print("origenal:\n",amber)
new = amber.reshape(2,6)
print("reshape Array\n",new)

