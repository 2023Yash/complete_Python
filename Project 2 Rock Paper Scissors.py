import random

def rock_paper_scissors(): 
  player = int(input("Write 1(Rock), 2(Paper) or 3(Scissors):"))
  computer = random.randrange(1,3)

  if(player == computer):
    print("Tie")
  else:
    if(player == 1 and computer == 2):
      print("Win")
    elif(player == 3 and computer == 2):

  return rock_paper_scissors()

rock_paper_scissors()