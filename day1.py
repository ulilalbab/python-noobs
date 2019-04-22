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

# Kaggle
print(5//2)
print(6//2)

# min & max
print(min(1,2,3))
print(max(1,2,3))

ages = [93 , 99, 66 ,17, 85 , 89, 77]
youngest = min(ages)
print(youngest)

# Floar
print(float(10))
print(int(3.33))
# even be called on strings!
print(int('807') + 1)


#Exercise: Syntax, Variables, & Numbers
print("Congratulations!")

pi = 3.14159
diameter = 3
radius = 0.5 * diameter
area = pi * radius^2
print(area)