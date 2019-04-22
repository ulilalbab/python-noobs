print("This line will be printed.")
#Simple World


# Indentation
x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")

# Exercise
print("Hello, World!")

# Integer
myint = 7
print(myint)

# floating number
myfloat = 7.0
print(myfloat)
myfloat=float(7)
print(myfloat)

# strings
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

# string with apostrophes
mystring = "Don't worry about apostrophes"
print(mystring)

# additional variations
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

# assignments with more than one variables
a,b = 3,4
print(a,b)

#assignment
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

