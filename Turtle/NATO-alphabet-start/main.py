#TODO 1. Create a dictionary in this format:
#  keys are the letters and the values are the code in csv file
import pandas as pd
{"A": "Alfa", "B": "Bravo"}
data = pd.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        output_list = [data_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()