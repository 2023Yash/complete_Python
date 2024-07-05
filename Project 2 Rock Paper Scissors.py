"""
Rock
Paper
Scissors
"""

import random

def rock_paper_scissors(): 
  player = int(input("Write 1(Rock), 2(Paper) or 3(Scissors):"))
  computer = random.randrange(1,3)

  print(f"You choosed {player}, computer choosed {computer}")

  if(player == computer):
    print("Tie")
  else:
    if(player == 1 and computer == 2 or player == 3 and computer == 2 or player == 1 and computer == 3):
      print("Win")
    elif(player == 2 and computer == 1 or player == 2 and computer == 3 or player == 3 and computer == 1):
      print("Loose")

  return rock_paper_scissors()

rock_paper_scissors()