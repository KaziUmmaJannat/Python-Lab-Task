import numpy as np

arr = np.array([1,2,3,2,4,2,5])

item = 2
n = 3

indexes = np.where(arr == item)[0]

print(indexes[n-1])