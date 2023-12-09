# Import libraries

import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

# Import data

data = json.load(open("data.json"))

# Create function that takes user input to search dictionary for entry.
# Verify if word is in dictionary by checking against input in lowercase, uppercase and title case. 
# If word is not in dictionary, search for possible matches.
# Confirm if possible match is the intended word.
# Generate error messages.

def search(word):
    if word.lower() in data:
        return data[word.lower()]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word.lower(), data.keys(), cutoff=0.8)) > 0:
        yn = input("Did you mean %s instead? Enter Y if Yes or N if No: " % get_close_matches(word.lower(), data.keys(), cutoff=0.8)[0])
        if yn.upper() == "Y":
            return data[get_close_matches(word.lower(), data.keys(), cutoff=0.8)[0]]
        elif yn.upper() == "N":
            return "Word not found. Please double check and try again."
        else:
            return "Input not recognized."
    elif len(get_close_matches(word.title(), data.keys(), cutoff=0.8)) > 0:
        yn = input("Did you mean %s instead? Enter Y if Yes or N if No: " % get_close_matches(word.title(), data.keys(), cutoff=0.8)[0])
        if yn.upper() == "Y":
            return data[get_close_matches(word.title(), data.keys(), cutoff=0.8)[0]]
        elif yn.upper() == "N":
            return "Word not found. Please double check and try again."
        else:
            return "Input not recognized."
    elif len(get_close_matches(word.upper(), data.keys(), cutoff=0.8)) > 0:
        yn = input("Did you mean %s instead? Enter Y if Yes or N if No: " % get_close_matches(word.upper(), data.keys(), cutoff=0.8)[0])
        if yn.upper() == "Y":
            return data[get_close_matches(word.upper(), data.keys(), cutoff=0.8)[0]]
        elif yn.upper() == "N":
            return "Word not found. Please double check and try again."
        else:
            return "Input not recognized."
    else:
        return "Word not found. Please double check and try again." 

# User inputs word to search

word = input(str("Input word: "))

# Display results
# Generate results as separate lines.
# Generate error messages as strings.

output = (search(word))

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)