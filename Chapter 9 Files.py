"""
Files
"""

username = input("Enter Username")
password_input = input("Enter Password:")

password_file = password_file = open("Projects/complete_Python/Chapter 9 Files.txt", "w")
password_file.write(f"{username}\n{password_input}")
password_file.close

password_file = open("Projects/complete_Python/Chapter 9 Files.txt")
file_data = password_file.readline()
print(file_data)
password_file.close()

"""
Practice
Set
"""