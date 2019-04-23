tup = 4, 5, 6
tup
nested_tup = (4, 5, 6), (7, 8)
nested_tup
print(nested_tup)





import numpy as np
data    = {i:np.random.randn() for i in range(7)}
data
print(data)

from numpy.random import randn
data1 = {i : randn() for i in range(7)}
print(data1)

# Append
a = [1,2,3]
b = a
a.append(4)
b
print(b)

# Append Element
def append_element(some_list, element):
    some_list.append(element)
data = [1, 2, 3]
append_element(data, 4)
data
print(data)

# Dynamic references
d = 5
type(d)
print(type(d)) # can identify class (int)

e = "Mantul Dab" # can identify as string
type(e)
print(type(e))






