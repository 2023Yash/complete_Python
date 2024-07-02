"""
Loops
"""

# For loop

for i in range(4):
    print(i)

for i in range(0, (10+1)):
    print(i)


for i in range(0, 100, 2):
    print(i)

# While Loop

w = 0

while (w < (30 + 1)):
    print(w)
    w += 1

# Printing a List

li = ["Jack", "John", "James", "Johny", "Jhonson"]
l = 0

while (l < len(li)):
    print(li[l])
    l += 1

for i in li:
    print(i)

# Printing a str

str = "2023yash"
s = 0

while (s < len(str)):
    print(str[s])
    s += 1

for i in str:
    print(i)

# for loop with else and continue

for i in range(5):
    if (i == 3):
        continue
    print(i)
else:
    print("done")

#break

for i in range(5):
    if (i == 3):
        break
    print(i)

"""
Practice
Set
"""

# Q.1 Write a program to print multiplication table of a given number using for loop.

table_of_number = int(input("Enter the no. of table:"))
till_what_number = int(input("Enter till where to multiply:"))

for i in range(1, (till_what_number + 1)):
    print(f" {table_of_number} * {i} = {table_of_number * i}")

# Q.2 Write a program to greet all the person names stored in a list ‘l’ and which starts with S.

name_list = ["Harry", "Soham", "Sachin", "Rahul"]

for i in name_list:
    if(i.startswith("S")):
       print("Hello", i)

# Q.3 Write a program to find whether a given number is prime or not.

prime_inp = int(input("Enter a no.:"))

for i in range(2, prime_inp):
    if(prime_inp % i == 0):
        print("no. is not prime")
        break
else:
    print("no. is prime")

# Q.4 Write a program to print the following star pattern.
# *
# ***
# ***** for n = 3

for i in range(1, 6, 2):
    print("*" * i)

# Q.5 Write a program to print the following star pattern:
# *
# **
# *** for n = 3

for i in range(1, 4):
    print("*" * i)

# Q.6 Write a program to print the following star pattern.
# ***
# * * for n = 3
# ***

for i in range(0, 3):
    if (i % 2 == 0):
        print("***")
    else:
        print("* *")