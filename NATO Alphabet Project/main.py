import pandas

# Read the CSV file containing the NATO phonetic alphabet into a DataFrame
data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary where each letter is the key and its corresponding code word is the value
nato_dict = {value['letter']: value['code'] for (key, value) in data_frame.iterrows()} # iterrows() loops over the DataFrame rows as (index, row) pairs

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a Word: ").upper()

"""
# Convert the user input into a list of phonetic code words. For each character in input, look up its code in dictionary.
# If the character exists in the dictionary, add its code word to the list
"""
phonetic_alphabet = [nato_dict.get(item) for item in user_input if item in nato_dict]
print(phonetic_alphabet)