import numpy as np

arr = np.array([5,-2,8,-6,3])

arr[arr < 0] = 0

print(arr)