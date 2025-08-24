from tkinter import *
import pandas
import random

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Times New Roman", 40, "italic")
WORD_FONT = ("Times New Roman", 60, "bold")

current_card = {} # Stores the current flashcard being shown
to_learn = {} # Stores the list of words that are left to learn

# ---------------------------- LOAD DATA ------------------------------- #

try: # Try loading the progress file if it exists
    old_data = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError: # If progress file doesn't exist, load the original French words file
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")

else: # If progress file exists, use it
    to_learn = old_data.to_dict(orient="records")

# ---------------------------- FLIP CARD ------------------------------- #
def flip_card():
    """Flip the flashcard to show the English translation."""

    canvas.itemconfig(canvas_background, image=back_image) # Change to back image
    canvas.itemconfig(label,text="English", fill="white") # Update language label
    canvas.itemconfig(word, text=current_card["English"], fill="white") # Show English word

# ---------------------------- NEXT CARD ------------------------------- #
def next_card():
    """Show the next random French word card."""

    global current_card, flip_timer
    window.after_cancel(flip_timer) # Cancel any existing timer so multiple timers don’t overlap
    current_card = random.choice(to_learn) # Pick a random word from the list

    # Display the French word and front image
    canvas.itemconfig(canvas_background, image=front_image)
    canvas.itemconfig(label, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")

    flip_timer = window.after(ms=3000, func=flip_card)  # Set a timer to flip the card after 3 seconds

# ---------------------------- WORD KNOWN ------------------------------- #
def is_known():
    """Remove known words from the list and save progress."""

    to_learn.remove(current_card) # Remove the current word from learning list
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False) # Save progress
    next_card() # Show the next card

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card) # Initial flip timer (to ensure card flips after 3 seconds)

# Flashcard canvas setup -------------------------- #
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png") # Front card image
back_image = PhotoImage(file="images/card_back.png") # Back card image
canvas_background = canvas.create_image(400, 263, image=front_image) # Place card image on canvas
canvas.grid(row=0, column=0, columnspan=2)

# Text on flashcards (title and word) -------------------------- #
label = canvas.create_text(400, 150, text="", font=TITLE_FONT)
word = canvas.create_text(400, 280, text="", font=WORD_FONT)

# Wrong button (user didn’t know the word) -------------------------- #
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, borderwidth=0, command=next_card)
wrong_button.grid(row=1, column=0)

# Right button (user knew the word) -------------------------- #
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, bg=BACKGROUND_COLOR, borderwidth=0, command=is_known)
right_button.grid(row=1, column=1)

next_card() # Start the first flashcard

window.mainloop()