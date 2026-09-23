import numpy as np 


arr = np.array([10,25,3.5,])
print(arr + 5) #add 5 to each element of the array
print(arr - 5) #subtract 5 from each element of the array
print(arr * 5) #multiply each element of the array by 5
print(arr / 5) #divide each element of the array by 5
print(arr ** 2) #square each element of the array
print(np.sqrt(arr)) #square root of each element of the array



"""
it will perform the operation on each element of the array and return a new array with the results.
much faster than using a for loop to perform the operation on each element of the array.
"""
