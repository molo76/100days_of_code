import pandas as pd

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data = pd.read_csv('nato_phonetic_alphabet.csv')
nato_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_alphabet)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_phonetic():
    word = input('Enter a word to convert: ').upper()
    try:
        phonemes = [nato_alphabet[char] for char in list(word)]
    except KeyError:
        print('Letters only please')
        generate_phonetic()
    else:
        print(phonemes)

generate_phonetic()