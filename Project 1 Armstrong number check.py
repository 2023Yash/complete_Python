'''
An Armstrong number is one whose sum of digits raised to the power three equals the number itself. 371
'''


def armstrong_number_check():
    inp = input("Enter a no. to check if a number is Armstrong Number:")
    result_str = 0

    for i in inp:
        result_str += int(i)**3
    else:
        if (int(inp) == result_str):
            print(f"🟢 {inp} is a Armstrong Number")
        else:
            print(f"🔴 {inp} is not a Armstrong Number")
        print()

    return armstrong_number_check()


armstrong_number_check()