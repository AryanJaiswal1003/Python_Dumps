from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

FONT = ("Times New Roman", 12, "bold")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """Generates a random secure password with letters, numbers, and symbols,
        inserts it into the password entry field, and copies it to clipboard."""

    # CHARACTERS FOR PASSWORD
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
               'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # GENERATE RANDOM CHARACTER USING LIST COMPREHENSION
    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbol + password_number # Combine all characters
    shuffle(password_list)  # Shuffle to make password unpredictable

    new_password = "".join(password_list) # Join list into a string
    password_entry.insert(0, new_password) # Insert password into the entry field
    pyperclip.copy(new_password) # Copy password to clipboard automatically

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """Saves the entered website, email, and password to a local file (data.txt).
        Checks for empty fields and confirms with user before saving."""

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website and email and password:  # Check if all fields are filled
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the Details Entered:\nEmail/Username: {email}\nPassword: {password}\nDo you want to Save?"
        ) # Ask confirmation before saving

        if is_ok:
            with open("data.txt", mode="a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n") # Append data into file

        messagebox.showinfo(title="Success", message="Password Entered is Saved.") # Show success message

        # Clear input fields for next entry
        website_entry.delete(0, 'end')
        email_entry.delete(0, 'end')
        password_entry.delete(0, 'end')
        website_entry.focus()  # Set cursor back to website field for quick entry

    else:  # Set cursor back to website field for quick entry
        messagebox.showwarning(
            title="Oops",
            message="Oops! Looks like you've missed a field.\nPlease make sure all fields are filled before proceeding."
        )

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

# Logo Image
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", font=FONT)
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", font=FONT)
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", font=FONT)
password_label.grid(row=3, column=0)

# Input Fields
website_entry = Entry(width=50)
website_entry.focus() # Set focus on website field when program starts
website_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=50)
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=32, justify="left")
password_entry.grid(row=3, column=1)

# Buttons
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()