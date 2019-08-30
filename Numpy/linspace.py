import numpy as np
from numpy import pi
print(np.linspace( 0, 2, 9 ))   # 9 numbers from 0 to 2

x = np.linspace( 0, 2*pi, 100 ) # useful to evaluate function at lots of points
f = np.sin(x)

print("******  x ? *******")
print(x)
print("******  f ? *******")
print(f)
