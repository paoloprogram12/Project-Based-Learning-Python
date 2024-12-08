# creates a story based on words that the user gives

with open("story.txt", "r") as f: # open functions allows python to open any file, (txt, json, etc.) "r" means to open it in read mode, "w" means creating a file (writing a file)
    story = f.read() # puts all the text into story variable

words = set() # stores words in set. A set is a data structure that is similar to a list but only contains unique elements
startOfWord = -1 # tells us if we found the starting index of a word

targetStart = "<"
targetEnd = ">"

# this for loop grabs all the words that have angle brackets
for i, char in enumerate(story): # gives access to the position and the element of the position
    if char == targetStart: # for loop starts when targetStart is found
        startOfWord = i

    if char == targetEnd and startOfWord != -1:
        word = story[startOfWord: i + 1] # slice operator
        words.add(word) # adds word into words list
        startOfWord = -1 # resets the start of words

# dictionary sets the unique words and creates values for them
answers = {}

# puts all the variables in the dictionary of unique words
for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

# replaces every word from the story variable containing <> to the words from the dictionary
for word in words:
    story = story.replace(word, answers[word]) # built in python function to replace words within an array

print(story)