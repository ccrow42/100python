# https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators

# https://en.wikipedia.org/wiki/Mersenne_Twister

# https://www.askpython.com/

# modules, can also be other files!!! see example. This is also why we should use main.py as the program entry point

import random
import pi_module

randomInteger = random.randint(1, 10)
randomFloat = random.random()
print(randomInteger)
print(randomFloat)
print(pi_module.pi)


# Lists
# lists can have different data types [ , ]
states = ["Delaware", "Pennsylvania", "New Jersey"]
#print (states.sort())
#print (states[-1])

print (states.pop())
print (states)
print (len(states))
# this is cool:
#names = names_string.split(", ")

# you can also nest lists


print(states.index("Delaware"))