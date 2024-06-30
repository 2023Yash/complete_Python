"""
Functions
and
Recursions
"""

# function

def avg():
    a = 1
    b = 2
    c = 3

    average = (1 + 2 + 3) / 3
    
    print(average)

avg() # function call

# function with argument

def avg2(a, b, c):
    average = (a + b + c) / 3
    return average;

print(avg2(23, 27, 11))

#default parameter

def greet(greeting="Hello", username="user"):
    print(greeting, username)

greet()

#recursion

# money = float(input("How much money do you have? "))

# def money_spent(money):
#   print()
#   amount_spent = float(input("Amount of money spent: "))
#   reason = input("Money spent on: ")
#   remaining_money = money - amount_spent
#   money = remaining_money
#   print("Amount of money left:", remaining_money)
#   return money_spent(money)

# money_spent(money)

"""
Practice
Set
"""

# Q.1 Write a python function to print first n lines of the following pattern:
# ***
# **
# *

def fliped_star_ladder(n):
    for i in range(1, (n)):
        print("*" * (n - i))

fliped_star_ladder(4)

def table():
    table_of_number = int(input("Enter the no. of table:"))
    till_what_number = int(input("Enter till where to multiply:"))

    for i in range(1, (till_what_number + 1)):
        print(table_of_number * i)

table()