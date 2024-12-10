# randomly generate math questions
# dont let user until its correct
# timed for each problem

import random

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12

def generateProblem():
    left = random.randint(MIN_OPERAND,MAX_OPERAND) # picks random numbers ranging from min to max
    right = random.randint(MIN_OPERAND, MAX_OPERAND) # picks random numbers ranging from min to max
    operator = random.choice(OPERATORS) # randomly picks an item from the list

    expr = str(left) + " " + operator + " " + str(right)
    print(expr)
    return expr

