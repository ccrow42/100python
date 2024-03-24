
#Global scope
enemies = 1

def increase_enemies():
  # if we want to modify the global variable:
  #global enemies
  # generally, don't do this!!! 
  # Local scope
  enemies = 2

  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Best practice, don't use the same variable name!

# For constants, use all uppercase verables. EG
URL = "https://www.ccrow.org"

