print ("Welcome to the tip calculator!")
bill = input("What was the total bill? ")
tipPercent = input("How much tip would you like to give (in %)? ")
people = input("How many people to split the bill? ")

amount = round (float(bill) * (float(tipPercent) * 0.01 + 1) / int (people), 2)
print ("Each person should pay: $" + str(amount))
