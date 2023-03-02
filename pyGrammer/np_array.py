import numpy as np

a = np.zeros((2, 2),dtype=int)
b = np.array([[1, 2], [3, 4]])
c = np.array([[1, 2], [5, 6]])
e=a+b+c
print(e.flatten())
