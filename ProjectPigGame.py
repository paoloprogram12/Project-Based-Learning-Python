import random

# roll function
def roll():
    # sets the minimum value for randomizer
    minValue = 1
    # sets the maximum value for randomizer
    maxValue = 6
    # sets the random int to roll variable
    roll = random.randint(minValue, maxValue)
    # returns the roll variable to the function
    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit(): # isdight() checks if input is a number
        players = int(players)  # converts players from a string into an integer
        if 2 <= players <= 4:
            break
        else:
            print("Must be a number between 2-4, try again.")
    else:
        print("Must be a number between 2-4, try again.")


maxScore = 25
playerScores = [0 for _ in range(players)] # for loop function to put the number of players into playerScores 

while max(playerScores) < maxScore: # max is a function to grab the maximum value of a list

    for playerIdx in range(players):
        print("\nPlayer " + str(playerIdx + 1) +  "'s turn!") # \n creates a line break
        print("Your total score is:", playerScores[playerIdx], "\n")
        currentScore = 0 # sets original score to 0

        while True:
            shouldRoll = input("Would you like to roll? (y)/(n)? ")
            if shouldRoll.lower() != "y": # converts input to lowercase
                break

            value = roll() # sets the number of what was rolled to value
            if value == 1: # if the value is 1, it moves to next person
                print("You rolled a 1! Turn done!")
                currentScore = 0
                break

            elif currentScore >= maxScore:
                break

            else:
                currentScore += value
                print("You rolled a:", value)

            print("Your score is:", currentScore)
         # adds the current score to the list depending on the player
        playerScores[playerIdx] += currentScore
        print("Your total score is:", playerScores[playerIdx])

             
       

maxScore = max(playerScores)
winner = playerScores.index(maxScore)
print ("The winner is Player", winner + "!")