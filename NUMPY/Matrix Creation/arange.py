"""
The np.arange() function creates an array of evenly spaced values within a given interval.
some similar to python range() function but np.arange() can handle float values as well.
The syntax of np.arange() is as follows:
np.arange(start, stop, step)
"""
import numpy as np

arr = np.arange(2, 12, 2) #start from 2 to 12 with step of 2
print(arr)

"""
used to make sequence of numbers with given start, stop and step values.
"""