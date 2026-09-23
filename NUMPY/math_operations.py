import numpy as np

"""
Here you can see im printing those values which can be
divisible by 2 okay ..... """
array = [10,20,35,47,51]

new_array = np.array([i for i in array if i%2==0])
print("Original array:", array)
print("New array:", new_array)

