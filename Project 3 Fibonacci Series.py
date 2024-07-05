"""
fibonacci series
"""

n = int(input("Enter the value of n:"))

old_num = 0
new_num = 1
result_str = ""

for i in range(0, int(n/2)):
    new_num += old_num
    old_num += new_num
    result_str += f"{old_num} + {old_num + new_num} + "
else:
    new_num += old_num
    old_num += new_num
    print(result_str + f"{old_num}")