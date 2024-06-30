"""
Conditional
Expression
"""

inp = int(input("Enter your Age:"))

if (inp >= 18):
    print("You are adult!\nGo get yourself a Job")
elif (inp < 18 and inp > 0):
    print("You are minor!")
else:
    print("⚠️ Ivalid Input!")

"""
Practice
Set
"""

# Q.1 Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user

std1 = int(input("Enter Student 1 Marks"))
std2 = int(input("Enter Student 2 Marks"))
std3 = int(input("Enter Student 3 Marks"))

if (std1 > 40):
    print("Student 1 Passed")
else:
    print("Student 1 Failed")

if (std2 > 40):
    print("Student 2 Passed")
else:
    print("Student 2 Failed")

if (std3 > 40):
    print("Student 3 Passed")
else:
    print("Student 3 Failed")

# Q.2 A spam comment is defined as a text containing following keywords: “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

inp_for_spam = input("Enter a comment:")

if ("Make a lot of money" in inp_for_spam or "buy now" in inp_for_spam or "subscribe" in inp_for_spam or "click" in inp_for_spam):
    print("includes spam")

# Q.3 Write a program to find whether a given username contains less than 10 characters or not

inp_for_name = input("Enter your name:")

if (len(inp_for_name) < 10):
    print("username contains less than 10 characters")
else:
    print("username doesn't contains less than 10 characters")

# Q.4 Write a program to calculate the grade of a student from his marks from the following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 => C
# 50 – 60 => D
# <50 => F

inp_for_marks = float(input("Enter marks for students"))

if (inp_for_marks < 0 or inp_for_marks > 100):
    print("⚠️ Ivalid Input!")
elif (inp_for_marks >= 90 and inp_for_marks <= 100):
    print("Excellent")
elif (inp_for_marks >= 80 and inp_for_marks <= 89):
    print("A")
elif (inp_for_marks >= 70 and inp_for_marks <= 79):
    print("B")
elif (inp_for_marks >= 60 and inp_for_marks <= 69):
    print("C")
elif (inp_for_marks >= 50 and inp_for_marks <= 59):
    print("D")
elif (inp_for_marks < 50):
    print("F")