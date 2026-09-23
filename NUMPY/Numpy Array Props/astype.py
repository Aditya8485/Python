import numpy as np

arr = np.array([1.1 , 2,7, 6, 8, 9, 10])
print(arr)
print(arr.dtype)


int_arr = arr.astype(int)
print(int_arr)
print(int_arr.dtype)


"""
astype() is used to convert the data type of an array.
It creates a new array with the specified data type.
"""