import numpy as np 


temp = np.array([[33.4 , 34.5, 35.6, 44.6, 45.7, 46.8, 47.9, 48.0]])

average_temp = np.mean(temp)
print("Average temperature:", average_temp)

average_temp = np.median(temp)
print("Average temperature:", average_temp)
