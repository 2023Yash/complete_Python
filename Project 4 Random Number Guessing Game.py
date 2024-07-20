"""
Random
Number
Guessing
Game
"""

import random

def Random_Number_Guessing_Game():
    random_number = random.randint(1, 100)
    print("Guess a number between 1️⃣  and 1️⃣ 0️⃣ 0️⃣  .")
    print()
    
    for i in range(5):
        guess_input = int(input("Guess 🤔 a number: "))
        if guess_input == random_number:
            print(f"You guessed the number right ✅ ! The number was {random_number}")
            break
        else:
            if guess_input > random_number:
                print("The number is smaller.")
            elif guess_input < random_number:
                print("The number is greater.")
    else:
        print(f"You guessed the number wrong ❌ ! The number was {random_number}")

Random_Number_Guessing_Game()