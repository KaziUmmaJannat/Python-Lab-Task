import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([5,2,7,4,9])

positions = np.where(a == b)

print(positions)