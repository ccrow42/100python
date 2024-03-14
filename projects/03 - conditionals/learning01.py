# this is where I am going to put my examples from the day

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please Pay $12")
else:
    print("You cannot ride the rollercoaster")

# >= > == <> !=
    
print ("end")