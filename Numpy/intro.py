#Num Sayı, Py Python
"""
https://www.numpy.org/devdocs/user/quickstart.html
Python içinde çok boyutlu dizinler olmadığı için geliştirilmiş bir kütüphane. (Numerical Python)
Numpy çok boyutlu diziler (Matris) oluşturur.
Matlab benzeri yetenekleri Numpy'a kazandırdı.
ndarray (N-dimensional array)
ufunc (Universal functions) Eleman başına işlem yapab bir fonksiyon
Numpy'ın en önemli özelliği array.
"""
import numpy as np
havadurumu = [[18,21,14],[23,17,28],[19,30,31]]
print(havadurumu)

a = np.arange(25)
print(a)

ab = np.arange(15).reshape(3,5)
print(ab)
print("Dimension Count: " + str(ab.ndim))


ac = np.arange(15).shape
print(ac)



