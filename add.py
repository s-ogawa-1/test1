#適当にコーディング

import numpy as np

def add(a, b):
    return a + b

x = add(5, 15)
print(x)

array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[10, 20], [30, 40]])
array3 = add(array1, array2)
print(array3)
