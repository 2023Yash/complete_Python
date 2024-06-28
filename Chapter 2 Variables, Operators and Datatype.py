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