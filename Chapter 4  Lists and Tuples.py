"""
Lists
and
Tuples
"""

mixed_list = [True, False, 42, 3.14, "Hello", "World"]

print(mixed_list[0])

# you can't replace letter in strings but you can change  the values of a list

mixed_list[0] = False
print(mixed_list[0])
print(mixed_list)

# you can index List like Strings

print(mixed_list[0:2])

# List Method

print(mixed_list.append("item")) # new item at the end

nums = [12, 23, 65, 2]

nums.sort()
print(nums) # sorts items

print(nums.reverse()) # reverse items

# tuples
# tuples are like strings. They can't be changed. You can only make a new tuple

names = ("John", "Jack", "James")

# tuples method

print(names.count("Jack"))
print(names.index("James"))

"""
Practice
Set
"""

# Q.1 Write a program to store seven fruits in a list entered by the user.

fruits = []

fruit1 = input("Enter fruit name:")
fruits.append(fruit1)
fruit2 = input("Enter fruit name:")
fruits.append(fruit2)
fruit3 = input("Enter fruit name:")
fruits.append(fruit3)
fruit4 = input("Enter fruit name:")
fruits.append(fruit4)
fruit5 = input("Enter fruit name:")
fruits.append(fruit5)
fruit6 = input("Enter fruit name:")
fruits.append(fruit6)
fruit7 = input("Enter fruit name:")
fruits.append(fruit7)

print(fruits)


# Q.2 Write a program to accept marks of 6 students and display them in a sorted manner.

marks = []

mark1 = input("Enter marks:")
marks.append(mark1)
mark2 = input("Enter marks:")
marks.append(mark2)
mark3 = input("Enter marks:")
marks.append(mark3)
mark4 = input("Enter marks:")
marks.append(mark4)
mark5 = input("Enter marks:")
marks.append(mark5)
mark6 = input("Enter marks:")
marks.append(mark6)
mark7 = input("Enter marks:")
marks.append(mark7)

print(marks)

# Q.3  Check that a tuple type cannot be changed in python.

tuple_Var = ("item", "item2")
# tuple_Var[0] = "item1" # throws error

# Q.4 Write a program to sum a list with 4 numbers.

def sum_of_list(numbers):
    total_sum = sum(numbers)
    return total_sum

numbers = [1, 2, 3, 4]
result = sum_of_list(numbers)
print(f"The sum of the list is: {result}")

# Q.5 Write a program to count the number of zeros in the following tuple:

a = (7, 0, 8, 0, 0, 9)

def count_zeros(t):
    return t.count(0)

zero_count = count_zeros(a)
print(f"The number of zeros in the tuple is: {zero_count}")
