import random

import numpy as np

print(np.zeros(10))

print(np.ones(10))

print(np.arange(10, 51))

print(np.arange(10, 51,2))


arr_0_8 = np.arange(0, 9)

print(arr_0_8.reshape(3,3))

print(np.eye(3))

print(np.random.rand(25))

mat = np.arange(1,26).reshape(5,5)
print(mat)

print(mat[0:,1][:3])
# [ 2  7 12]

print(mat[4])
# [21 22 23 24 25]

print(mat[3:])

print(mat.sum())

print(mat.std())

print(mat.sum(axis=0))


