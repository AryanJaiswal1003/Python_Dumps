## NATO Phonetic Alphabet Converter

This project converts any word entered by the user into its NATO phonetic alphabet code words. For example, the word CAT 
    will be converted into ['Charlie', 'Alpha', 'Tango'].

---

## Features
    
    * Reads a CSV file (nato_phonetic_alphabet.csv) containing the phonetic alphabet mapping (letters → code words).
    * Uses a dictionary comprehension to create a lookup dictionary.
    * Accepts user input and converts each letter into its corresponding NATO code word.
    * Ignores characters not present in the phonetic alphabet.

---

## 📂 File Structure

    ├── nato_phonetic_alphabet.csv   # CSV file containing the phonetic alphabet
    ├── main.py                      # Main Python script
    └── README.md                    # Project documentation