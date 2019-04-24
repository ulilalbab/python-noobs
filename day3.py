def isiterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False
isiterable('a string')
print(isiterable('a string'))

import some_module
result = some_module.f(5)
pi = some_module.PI
print(pi)

from some_module import f, g, PI
result = g(5, PI)
print(result)

# import different variables names

import some_module as sm
from some_module import PI as pi, g as gf
r1 = sm.f(pi)
r2 = gf(6, pi)

print(r1)
print(r2)

a = [1, 2, 3]
b = a
c = list(a)

a is b

a is not b
print(a is b)
print(a is not c)

import math #import module first
print(math.sqrt(9))

#floor math
x = 33.7
y = 40.65

print ("The floor of 33.7 is :", end = "")
print (math.floor(x))
print ("The floor of 40.65 is :", end = "")
print (math.floor(y))

#numeric types
ival = 17239871
ival ** 6
print(ival ** 6)

#Page 39 (Strings)

# 64 bit value
fval = 7.243
fval2 = 6.78e-5
print(fval2)
