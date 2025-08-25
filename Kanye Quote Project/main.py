from tkinter import *
import requests
from dotenv import load_dotenv
import os

FONT = ("Times New Roman", 20, "bold")

# ---------------------------- LOAD SECRETS ---------------------------- #
load_dotenv() # Load environment variables from the .env file
kanye_api = os.getenv("KANYE_API") # Retrieve the Kanye API endpoint from the environment

# ---------------------------- API FUNCTION ---------------------------- #
def get_quote():
    """
       Fetches a random Kanye West quote from the API and updates the GUI canvas.
   """
    response = requests.get(kanye_api)  # Make a GET request to the API
    response.raise_for_status() # Raise an error if the request fails
    quote = response.json()["quote"] # Extract the "quote" field from the JSON response

    canvas.itemconfig(quote_text, text=quote) # Update the text on the canvas with the new quote

# ---------------------------- UI SETUP -------------------------------- #
# Create the main window
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

# Setup the canvas with background image
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)

# Placeholder text for the quote (will be updated by get_quote)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=FONT, fill="black")
canvas.grid(row=0, column=0)

# Add a button with Kanye's face, fetches a new quote when clicked
kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, borderwidth=0, command=get_quote)
kanye_button.grid(row=1, column=0)

get_quote() # Fetch the first quote automatically on startup

window.mainloop()