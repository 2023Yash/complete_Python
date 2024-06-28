"""
Variables,
Operaters
and
Datatypes
"""

#ways to write strings

a = 'str'
b = "str"
c = '''
str
str
str
'''
d = """
str
str
str
"""

# str function

d_string_lenth = len(d)
print(d_string_lenth)
print(d.startswith("s"))
print(d.endswith("s"))
print(d.capitalize())

# str slicing, !!!Last will not be included

print(a[1], a[0:3], a[-1: -3])
print(a[0:], a[:3])

#skiping

num_str = "0123456789"
print(num_str[0:9:2])#prints even numbers

# Escape sequence character

print("I LIKE\n\t\"Git hub\"")


"""
Practice
Set
"""

# Q.1 Write a python program to display a user entered name followed by Good Afternoon using input () function.

name_input = input("Enter Your Name:")
print("Good Afternoon", name_input.capitalize())

# Q.2 Write a program to fill in a letter template given below with name and date.

print(
'''
Dear <|Name|>,
You are selected!
<|Date|>
'''
)
date = input("Enter a date:")
print("Dear", name_input,",\nYou are selected!\n", date)

# Q.3 Write a program to detect double space in a string.

string = "double  space"
print("  " in string)

# Q.4 Replace the double space from problem 3 with single spaces .

string2 = "single space"
print(" " in string2)

# Q.5 Write a program to format the following letter using escape sequence characters.

print("\t\tDear Yash,\n\tthis python course is nice.\n\t\t Thanks!")