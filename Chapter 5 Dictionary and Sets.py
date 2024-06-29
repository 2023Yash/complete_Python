"""
Dictionary
and
Sets
"""

marks = {
    "James": 100,
    "John": 90,
    "Jack": 69,
}

print(marks["Jack"])

# Dictionary Methods

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"james": 99, "Jackson": 100})
print(marks)
print(marks.get("james"))

# set (no elements cant repeat in set)

sets = {1, 2, 3, 3, 3}
print(sets)

empty_set = set()
print(empty_set, type(empty_set))

# set Methods

empty_set.add("item")
print(empty_set)

print(empty_set.len())

empty_set.remove("item")
print(empty_set)

# .pop() remove random item from set

"""
Practice
Set
"""

# Q.1 Write a program to create a dictionary of Hindi words with values as their English translation.

words = {
    "billi": "cat",
    "kutta": "dog"
}

inp = input("Enter a word:")

print[words[inp]]