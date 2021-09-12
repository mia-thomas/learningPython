''' The main goal of the project is to create a program that randomly select a number in a range then the user has to guess the number. user has three chances to guess the number if he guess correct then a message print saying “you guess right “otherwise a negative message prints.
Topics: random module, for loop, f strings '''

import random
print("Welcome to the Number Guessing Game, lets begin with numbers between 1 and 10!")
userInput=()
print("Would you like to play?")
userChoice= input("Yes or No?").lower()
number=str(random.randint(1,10))

def guess_game():
    while userChoice == "yes":
        number=str(random.randint(1,10))
        userInput=(input("Please pick a Number between 1 and 10\n"))
        if userInput == number:
            print("You guessed Correct!")
            print("The Number was " + number)
            print("Congratulations! You won the game!")
            break
        else:
            print("Oops try again! the numbers did not match")
            print("the Number was " + number)

guess_game()
