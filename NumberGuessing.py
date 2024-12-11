# Guesses a number between 1 and 100:

import random

number = random.randint(1, 100)

while True:
    try: # try and except handles if the input isn't a number
        theGuess = int(input("Guess the number between 1 and 100: "))

        if theGuess < number:
            print("Too Low!")
        elif theGuess > number:
            print("Too High!")
        else:
            print("Congratulations! You have guessed " + str(number) + "!")
            break

    except ValueError:
        print("Please Enter a Valid Number.")
    # guess = int(theGuess) # to convert theGuess into a int


        
