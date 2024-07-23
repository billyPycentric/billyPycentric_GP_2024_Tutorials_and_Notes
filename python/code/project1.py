import sys , random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print('')
player_choice = input("Enter ...\n1. for Rock,\n2. for Paper,\n3. for Scissors :\n\n")

player = int(player_choice)

if player < 1 | player > 3:
    sys.exit(print("You must Enter 1, 2 or 3."))

computer_choice = random.choice("123")

computer = int(computer_choice)

print('')
print("You chose " + str(RPS(player)).replace("RPS.","") + " .")
print("Computer chose " + str(RPS(computer)).replace("RPS.","") + " .")
print('')

if(player == 1 and computer == 3):
    print("You win!")
elif(player == 2 and computer == 1):
    print("You win!")
elif(player == 3 and computer == 2):
    print("You win!")
elif(player == computer):
    print("Its a tie")
else:
    print("Python wins")

print('')
