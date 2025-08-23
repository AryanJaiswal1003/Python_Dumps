import pandas

# Read the CSV file containing the NATO phonetic alphabet into a DataFrame
data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary where each letter is the key and its corresponding code word is the value
nato_dict = {value['letter']: value['code'] for (key, value) in data_frame.iterrows()} # iterrows() loops over the DataFrame rows as (index, row) pairs

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
if_true = True

while is_true:
  user_input = input("Enter a Word: ").upper()
  """
  # Convert the user input into a list of phonetic code words. For each character in input, look up its code in dictionary.
  # If the character exists in the dictionary, add its code word to the list
  """
    try:
        phonetic_alphabet = [nato_dict[letter] for letter in user_input] # Try to convert each letter to its NATO phonetic code
        print(phonetic_alphabet)
        is_true = False  # Stop loop after successful conversion

    except KeyError:
        print("Sorry, only Letters in the alphabet please.\n")
