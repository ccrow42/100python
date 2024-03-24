#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import art
import random

print (art.logo)

game_end = False

difficulty = input ("Would you like to play an easy or hard game? ")
if difficulty == "easy":
    lives = 10
elif difficulty == "hard":
    lives = 5
else:
    print ("invalid entry")
    lives = 0
    game_end = True
    win = False

    
number = random.randint(1,101)


while not game_end:

    guess = int(input("I'm thinking of a number between 1 and 100. Guess: "))
    if guess > number:
        print ("You guessed too high")
        lives -= 1
        print (f"You now have {lives} lives")
    elif guess < number:
        print ("You guessed too low")
        lives -= 1
        print (f"You now have {lives} lives")
    elif guess == number:
        print ("You guessed it!")
        win = True
        game_end = True
    
    # Check lives
    if lives == 0:
        win = False
        game_end = True


if win:
    print ("You win!")
else: print (f"You loose, the number was: {number}")

