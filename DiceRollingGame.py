import random

def diceRoller():
    numOne = random.randint(1, 6)
    numTwo = random.randint(1, 6)
    return numOne, numTwo


playingGame = True
while playingGame:
    choice = input("Roll the dice? (y/n): ").lower() # .lower() always changes the input to a lowercase

    if choice == "y":
        dice = diceRoller()
        print(dice)
        pass
    elif choice == "n":
        print("Thanks for playing!")
        playingGame = False
    else:
        print("Invalid choice!")