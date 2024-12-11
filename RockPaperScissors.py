# Rock Paper Scissors
import random

choices = ("r", "p", "s")
items = {"r": "Rock", "s": "Scissors", "p": "Paper"} # dictionary
while True:
    choice = input("Rock, Paper, or Scissors? (r/p/s): ").lower()
    if choice not in choices:
        print("Invalid Choice!")
        continue # Restarts the while loop
    computerChoice = random.choice(choices) # chooses a random item from the list

    print("You chose " + items[choice] + "!") # chooses from items from the dictionarty
    print("Computer chose " + items[computerChoice] + "!")
    
    if choice == computerChoice:
        print("You have Tied!")
    elif \
    (choice == "r" and computerChoice == "s") or \
    (choice == "p" and computerChoice == "r") or \
    (choice == "s" and computerChoice == "p"):
        print("Congratulation! You have won!")
    elif \
    (choice == "r" and computerChoice == "p") or \
    (choice == "p" and computerChoice == "s") or \
    (choice == "s" and computerChoice == "r"):
        print("Unfortunately, you have Lost.")
    
    playAgain = input("Would you like to play again? (y/n): ").lower()

    if playAgain == "n":
        print("Thanks for playing!")
        break

    
    