"""
Variables,
Operaters
and
Datatypes
"""

# Variables are like containers to store datatype

# All types of datatype

a = 14            # Integer
b = 3.23          # Float
__name__ = "yash" # String
yash = True       # Booleaan (True / False)
no = False        # Booleaan (True / False)
no_thing = None   # None

# This added a + b + 3 (20.23) converted it to string and added yash, a string.

print(str(a + b + 3) + __name__)

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

print(type(a))
print(type(b))
print(type(__name__))
print(type(no))
print(type(no_thing))

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

print(a > b)

# Q.5 Write a python program to find an average of two numbers entered by the user.

num_x = int(input("Enter no. 1:"))
num_w = int(input("Enter no. 2:"))
print((num_x + num_w) / 2)

# Q.6 Write a python program to calculate the square of a number entered by the user.

num_v = int(input("Enter a no. :"))

print(num_v ** 2)