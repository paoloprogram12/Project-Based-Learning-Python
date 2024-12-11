# Guesses a number between 1 and 100:

import random

number = random.randint(1, 100)

while True:

    theGuess = int(input("Guess the number between 1 and 100: "))
    guess = int(theGuess) # to convert theGuess into a int

    if guess == number:
        print("Congratulations! You have guessed " + str(number) + "!") # to convert number into a string
        print("Thanks for playing!")
        break
    elif guess > 100 or guess < 1:
        print("Invalid Number, Try Again!")
    elif guess >= 1 and guess <= 100 and guess != number:
        print("Wrong Number! Try Again!")
        
