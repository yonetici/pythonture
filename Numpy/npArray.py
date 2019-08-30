import numpy as np


a = np.array([1,2,3,4,5,6,7,8,9])
a = a.reshape(3,3)
print(a)
print(a.ndim) #1
print(a.dtype)
"""
a = np.array([1,2,3,4,5,6,7,8,9]) > int32
a = np.array([1,"2",3,4,5,6,7,8,9]) > U11
a = np.array([1.9,2,3,4,"5",6,7,8,9]) > U32
a = np.array([1.9,2,3,4,5,6,7,8,9]) > float64
"""

b = np.array([[1,3],[5,7],[9,11]])
print(b.ndim) #2