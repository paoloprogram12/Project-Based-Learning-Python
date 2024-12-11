# randomly generate math questions
# dont let user until its correct
# timed for each problem

import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generateProblem():
    left = random.randint(MIN_OPERAND,MAX_OPERAND) # picks random numbers ranging from min to max
    right = random.randint(MIN_OPERAND, MAX_OPERAND) # picks random numbers ranging from min to max
    operator = random.choice(OPERATORS) # randomly picks an item from the list

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr) # evaluates a string as if it was a python expression
    return expr, answer

wrong = 0
input("Press enter to start!")
print("----------------------")

startTime = time.time() # gives us a timestamp in seconds

# prints out problems and answers
for i in range(TOTAL_PROBLEMS):
    expr, answer = generateProblem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ") # converting int into a string
        if guess == str(answer): # convert into a string b/c answer is originally a int. guess is a string and comparing a string and a int wouldn't work
            break
        wrong += 1

endTime = time.time()
totalTime = round(endTime - startTime, 2)

print("----------------------")
print("Nice work! You finished in", totalTime, "seconds!")
print("You got", wrong, "wrong!")