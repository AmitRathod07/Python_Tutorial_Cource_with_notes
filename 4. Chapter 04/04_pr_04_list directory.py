# Author : Amit
# Location : Mars
# Date : 07/12/2022
     # ctrl + '/' to do selected text into comment.. 
# import os
# print(os.listdir())

import numpy
arr = numpy.array([1, 2, 3])
print(arr)

import numpy as np
arr1=np.array([5, 4, 8])
print(arr1)

print(type(arr1))

import numpy as np

print(np.__version__)

#------------------------------------
import numpy as np

a = np.array(42) #0D
b = np.array([1, 2, 3, 4, 5])  #1D
c = np.array([[1, 2, 3], [4, 5, 6]])  #2D
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])  #3D

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#--------------------------------------

arr = np.array([1, 2, 3, 4])
print(arr[0])

arr = np.array([1, 2, 3, 4])
print(arr[1])

# as well as in 2D, #d Or further

#-------------------------------------------
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])

# Do slicing as well as in all Dimentions

#----------------------------------------------
'''
Data Types in Python
By default Python have these data types:

strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"
integer - used to represent integer numbers. e.g. -1, -2, -3
float - used to represent real numbers. e.g. 1.2, 42.42
boolean - used to represent True or False.
complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j
Data Types in NumPy
NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.

Below is a list of all data types in NumPy and the characters used to represent them.

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
'''



print(arr.dtype)

import numpy as np

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)