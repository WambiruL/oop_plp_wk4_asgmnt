import json
import difflib
import random

#load the dict data from the Json file
def load_data():
    with open("data.json") as file:
        return json.load(file)
    
#function to get the definition of a word
def get_definition(word, dictionary):
    # Normalize the word to lower case
    word = word.lower()
    if word in dictionary:
        definition = dictionary[word]
        
        # Check if the definition is a list (multiple meanings)
        if isinstance(definition, list):
            return random.choice(definition)  # Randomly choose one definition
        else:
            return definition  # Return single definition if not a list
    else:
        # If the word is not found, suggest a close match
        suggestion = get_close_matches(word, dictionary)
        return f"Word not found. {suggestion}"
    
#function to suggest close matches for misspelled words
def get_close_matches(word, dictionary):
    matches = difflib.get_close_matches(word, dictionary.keys(), n=1, cutoff = 0.7)
    if matches and len(matches[0]) > 1:
        return f"Did you mean '{matches[0]}'?"
    else:
        return "No close match found."
    
#main program
def main():
    dictionary = load_data()
    while True:
        word =input("Enter a word(or type 'exit' to quit): ")
        if word.lower() == 'exit':
            break
        definition = get_definition(word, dictionary)
        print(definition)

if __name__ == "__main__":
    main()
    