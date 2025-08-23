import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    """Search for a website in data.json and show saved email & password."""

    search = website_entry.get().title() # Get input & convert to Title Case
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file) # Load saved credentials
            if search in data: # If website exists in file
                saved_data = data[search]
                messagebox.showinfo(
                    title=search,
                    message=f"Email: {saved_data["email"]}\nPassword: {saved_data["password"]}"
                )

            else: # If website not found
                messagebox.showerror(
                    title="Error",
                    message=f"No Details for the Website {search} Exists."
                )

    except FileNotFoundError: # If data.json doesn’t exist yet
        messagebox.showerror(title="Error", message="No Data File Found in the Database")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    """Generate a strong random password, insert into Entry, and copy to clipboard."""

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Randomly pick letters, numbers, and symbols
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    # Combine and shuffle
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list) # Convert list → string

    # Insert into entry box & copy to clipboard
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """Save the current website/email/password into a JSON file (data.json)."""

    website = website_entry.get().title()  # Standardize to Title Case
    email = email_entry.get()
    password = password_entry.get()

    # New entry to add
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    # Validation: Ensure required fields aren’t empty
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try: # Try to read existing data
            with open("data.json", mode= "r") as data_file:
                data = json.load(data_file) # Reading Old Data

        except FileNotFoundError: # If file doesn’t exist, create it and dump new_data
            with open("data.json", mode= "w") as data_file:
                json.dump(new_data, data_file, indent=4) # Creates New JSON File

        else: # Updating old data with new data
            data.update(new_data)
            with open("data.json",mode="w") as data_file:
                json.dump(data, data_file, indent=4) # Saving the updated data

        finally: # Clear input fields after saving
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            email_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

######### Logo #########
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

########## Labels ##########
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

######### Entries #########
website_entry = Entry(width=31)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=50)
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=31)
password_entry.grid(row=3, column=1)

######### Buttons #########
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text= "Search", width=15, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()