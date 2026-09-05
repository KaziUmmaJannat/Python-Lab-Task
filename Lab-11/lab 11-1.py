import numpy as np

arr = np.array([12,5,8,1,19,3])

k = 3

smallest = np.partition(arr,k)[:k]

print(smallest)