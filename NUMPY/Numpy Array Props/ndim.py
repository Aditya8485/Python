"""
ndim stands for number of dimensions of the array.
It returns an integer value which represents the number of dimensions of the array.
"""
import numpy as np

arr_1d = np.array([10, 15, 20, 25, 30])
arr_2d = np.array([[10, 15, 20], [25, 30, 35]])
arr_3d = np.array([[[10, 15, 20], [25, 30, 35]], [[40, 45, 50], [55, 60, 65]]])

print("Number of dimensions in 1D array:", arr_1d.ndim)
print("Number of dimensions in 2D array:", arr_2d.ndim)
print("Number of dimensions in 3D array:", arr_3d.ndim)

"""
it helps where , like if you want to know the data is stored in
form of list or like table form or like a llayered form , then you can use ndim to know the number of dimensions of the array.
"""
