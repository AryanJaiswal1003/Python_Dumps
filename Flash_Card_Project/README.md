## Flashy – French Flashcards

Flashy is a Python flashcard application built with Tkinter and Pandas.
It helps you learn French vocabulary by showing random French words and flipping them to reveal the English translation.

When you mark a word as known, it gets removed from the learning list, and your progress is saved automatically.

---

## Features

    1. Randomly displays French words with their English translations.
    2. Automatic card flip after 3 seconds.
    3. Save your progress – known words are removed and stored in words_to_learn.csv.
    4. Clean UI with interactive buttons (✔️ Known / ❌ Unknown).

---

## Project Structure
    flashy/
    │── data/
    │   ├── french_words.csv       # Original word list (French → English)
    │   ├── words_to_learn.csv     # Progress file (auto-generated after first run)
    │
    │── images/
    │   ├── card_front.png         # Front side of flashcard
    │   ├── card_back.png          # Back side of flashcard
    │   ├── right.png              # Checkmark button
    │   ├── wrong.png              # Cross button
    │
    │── main.py                    # Main application code

---

## How It Works

    1. The app shows a French word.
    2. After 3 seconds, the card flips to show the English translation.
    
    3. Click:
           ❌ (Don’t Know) → Keep the word in the learning list.
           ✔️ (Know It) → Remove the word and save progress.
    
    4. Your progress is saved in data/words_to_learn.csv, so next time you only study the remaining words.

---