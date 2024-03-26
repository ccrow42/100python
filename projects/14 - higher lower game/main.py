from data import data
import art
import random
# Intro Logo
print (art.logo)

# Game is played for 10 rounds.

# Function ideas:
# compare
#   returns array element that is higher

elements = len(data)
score = 0
game_end = False

def print_vs(choice_a, choice_b):
    """Prints the vs choices.
    choice_a: numeric data array element
    choice_b: numeric data array element
    """
    print (f"{data[choice_a]["name"]} - {data[choice_a]["description"]} from the {data[choice_a]["country"]}")
    print (art.vs)
    print (f"{data[choice_b]["name"]} - {data[choice_b]["description"]} from the {data[choice_b]["country"]}")


def eval(choice_a, choice_b, choice):
    """Function takes 3 elements:
    choice_a: numeric data array element
    choice_b: numeric data array element
    choice: users choice (should be string lowercase a or b)
    
    returns a true if the user was correct and false if incorrect"""
    
    if choice == "a":
        if data[choice_a]["follower_count"] > data[choice_b]["follower_count"]:
            return True
        else:
            return False
    if choice == "b":
        if data[choice_a]["follower_count"] < data[choice_b]["follower_count"]:
            return True
        else:
            return False

for round in range(1,11):

    choice_a = random.randint (0, elements)
    choice_b = random.randint (0, elements)
    print_vs(choice_a, choice_b)

    choice = input("Choose: (A/B): ").lower()
    result = eval (choice_a, choice_b, choice)
    if result:
        print ("Correct!")
        score += 1
        print (f"Your score is: {score}")
    else:
        print ("Incorrect!")
        print (f"Your score is: {score}")

print (f"Your final score is: {score}")




# This could be a function, send the element numbers, choice, return true or false



    

