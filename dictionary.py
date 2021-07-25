import json
from difflib import get_close_matches


data = json.load(open("data.json"))

def translate(word):
    if wordInData(word) == False:
        if len(get_close_matches(word, data.keys())) > 0:
            choice = input("Did you mean %s instead? Enter Y if yes, or N if no:" % get_close_matches(word, data.keys())[0])
            choice = choice.lower()
            return choiceForMatchingWord(choice, word)
            
        else:
            return "The word doesn't exist. Please check your input."
    else:
        return wordInData(word)

# check if word is in data
def wordInData(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        return False

# get user choice for matching word
def choiceForMatchingWord(choice, word):
    if choice == "y":
        return data[get_close_matches(word, data.keys())[0]]
    elif choice == "n":
        return "The word doesn't exist. Please check your input."
    else:
        return "Invalid entry."

# output results
def outputResult(output):
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)

# get user word input
word = input("Enter a word: ").lower()

output = translate(word)
outputResult(output)
