#np.shape() is used to get the shape of the array
"""
it returns a tuple of array dimensions (number of elements along each axis).
it can be helpful to understand the structure of the array and how to manipulate it.
when you will work on multi-dimensional arrays, it will be very useful to know the shape of the array.
"""


import numpy as np 

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(np.shape(arr_2d))
