tup = 4, 5, 6
tup
nested_tup = (4, 5, 6), (7, 8)
nested_tup
print(nested_tup)

a = 5
a
print(a)



import numpy as np
data    = {i:np.random.randn() for i in range(7)}
data
print(data)

from numpy.random import randn
data1 = {i : randn() for i in range(7)}
print(data1)