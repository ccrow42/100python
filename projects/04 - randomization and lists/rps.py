rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

player = int(input("Input 1 for Rock, 2 for Paper, and 3 for Scissors"))
computer = random.randint(1, 3)
print (f"You played: {player}, the computer played: {computer}")
result = player - computer
if result == 0:
    print ("Tie!")
elif result == -1:
    print ("You lose!")
elif result == -2:
    print ("You win!")
elif result == 1:
    print ("You Win!")
elif result == 2:
    print ("You Lose!")
