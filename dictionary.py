import json
from difflib import get_close_matches


data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        choice = input("Did you mean %s instead? Enter Y if yes, or N if no:" % get_close_matches(word, data.keys())[0])
        choice = choice.lower()
        if choice == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif choice == "n":
            return "The word doesn't exist. Please check your input."
        else:
            return "Invalid entry."
    else:
        return "The word doesn't exist. Please check your input."

# get user word input
word = input("Enter a word: ").lower()

print(translate(word))