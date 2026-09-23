"""
#.dtype it is used to check the data type of the array elements.
it returns the data type of the array elements.
it can check the nature of the data stored in the array and can be useful for debugging and understanding the data.
"""

import numpy as np

arr_1d = np.array([10, 15, 20, 25, 30,])
arr_2d = np.array([[10.56, 15, 20], [25, 30, 35]])


print("Data type of elements in 1D array:", arr_1d.dtype)
print("Data type of elements in 2D array:", arr_2d.dtype)



"""
this can be used where , like you want to make sure
that all values should be integer or float or string or boolean etc..
then you can use dtype to check the data type of the array elements.
"""


"""
let me show you last one thats boolean type
"""
arr_bool = np.array([True, False, True, False])
print("Data type of elements in boolean array:", arr_bool.dtype)