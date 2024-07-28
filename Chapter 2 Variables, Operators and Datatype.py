"""
Variables,
Operaters
and
Datatypes
"""

# Variables are like containers to store datatype

# All types of datatype

data_type_var = "Hello World"	                         # string
data_type_var = 20	                                     # integer
data_type_var = 20.5	                                 # float
data_type_var = 1j	                                     # complex
data_type_var = ["apple", "banana", "cherry"]	         # list
data_type_var = ("apple", "banana", "cherry")	         # tuple
data_type_var = range(6)	                             # range
data_type_var = {"name" : "John", "age" : 36}	         # dictionary
data_type_var = {"apple", "banana", "cherry"}	         # set
data_type_var = frozenset({"apple", "banana", "cherry"}) # frozen set
data_type_var = True	                                 # boolean
data_type_var = b"Hello"	                             # bytes
data_type_var = bytearray(5)	                         # byte array
data_type_var = memoryview(bytes(5))	                 # memory view
data_type_var = None                                     # none

# Setting a specific data type

specific_data_type_var = str("Hello World")	                       # string
specific_data_type_var = int(20)	                                 # integer
specific_data_type_var = float(20.5)	                             # float
specific_data_type_var = complex(1j)	                             # complex
specific_data_type_var = list(("apple", "banana", "cherry"))	     # list
specific_data_type_var = tuple(("apple", "banana", "cherry"))	     # tuple
specific_data_type_var = range(6)	                                 # range
specific_data_type_var = dict(name="John", age=36)	               # dictionary
specific_data_type_var = set(("apple", "banana", "cherry"))	       # set
specific_data_type_var = frozenset(("apple", "banana", "cherry"))  # frozen set
specific_data_type_var = bool(5)	                                 # boolean
specific_data_type_var = bytes(5)	                                 # bytes
specific_data_type_var = bytearray(5)	                             # byte array
specific_data_type_var = memoryview(bytes(5))	                     # memory view

# This added a + b + 3 (20.23) converted it to string and added yash, a string.

# print(str(a + b + 3) + __name__)


"""
#Arithmatics Operators

print(a + b) # +
print(a - b) # -
print(a * b) # *
print(a / b) # /

# Assignment Operators

a += b
a -= b

# Comparision Operators

a == b
a != b
a < b
a <= b
a > b
a >= b
"""

# Logical Operators

print("True and False =", True and False)
print("False and True =", False and True)
print("True and True =", True and True)
print("False and False =", False and False)

print("True or False =", True or False)
print("False or True =", False or True)
print("True or True =", True or True)
print("False or False =", False or False)

print(not(True))
print(not(False))

# How to Get Type

print(type(data_type_var))

# Assign multiple values

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Global Variable

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

"""
Practice
Set
"""

# Q.1 program to add two numbers.

num_a = int(input("Enter no. 1:"))
num_b = int(input("Enter no. 2:"))
print(num_a + num_b)

# Q.2 program to find remainder when a number is divided by z.

num_y = int(input("Enter no. 1:"))
num_z = int(input("Enter no. 2:"))
print(num_y % num_z)

# Q.3 Check the type of variable assigned using input () function.

var_name = input("Enter something:")
print(type(var_name))

# Q.4 Use comparison operator to find out whether ‘a’ given variable a is greater than ‘b’ or not.

a = 20
b = 10

print(a > b)

# Q.5 Write a python program to find an average of two numbers entered by the user.

num_x = int(input("Enter no. 1:"))
num_w = int(input("Enter no. 2:"))
print((num_x + num_w) / 2)

# Q.6 Write a python program to calculate the square of a number entered by the user.

num_v = int(input("Enter a no. :"))

print(num_v ** 2)