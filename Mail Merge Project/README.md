## Mail Merge Project

This project demonstrates a simple Mail Merge program using Python. It reads a list of invited names from a text file, merges 
    each name into a pre-written letter template, and generates personalized letters for each guest.

---

## How It Works

1. Input Files

       * Input/Names/invited_names.txt
            --> Contains the list of names to be invited (one name per line).
    
       * Input/Letters/starting_letter.txt
            --> Contains the base letter template with a placeholder [name].

2. Process

       * The program reads the template letter.
       * Iterates over each name in the invited_names.txt.
       * Replaces the placeholder [name] with the actual guest’s name.
       * Saves each personalized letter as a new .txt file.

3. Output

       * The personalized letters are saved in the Output/ReadyToSend/ directory.
       * Each file is named after the invited person.

---

## File Structure
    Mail Merge Project/
    │
    ├── Input/
    │   ├── Names/
    │   │   └── invited_names.txt
    │   ├── Letters/
    │   │   └── starting_letter.txt
    │
    ├── Output/
    │   └── ReadyToSend/
    │       └── [Generated personalized letters here]
    │
    ├── main.py   # Python script for mail merge
    └── README.md # Documentation

---