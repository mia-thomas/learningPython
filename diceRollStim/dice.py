
print("Welcome to my Dice Stimulator! Lets begin")


import random
while True:
    print("You have two options..")
    print("1 = Roll The Dice")
    print("2 = Exit")
    userInput = int(input("What do you want to do?\n"))
    if userInput == 1:
        number = str(random.randint(1,6))
        print("Congratulations! You have roled the number " + number + "!\n")
        print("would you like to roll again?")
        print("Would you like to roll again?")
    else:
        break