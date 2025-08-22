from tkinter import *

FONT = ("Times New Roman", 12, "bold")

# Function to convert miles to kilometers
def converter():
    miles = user_input.get() # Get input from Entry widget
    km = float(miles) * 1.609344
    converter_label["text"] = f"{km}"

# Create main window
window = Tk()
window.title(string="Mile to Km Converter")
window.config(pady=20, padx=20) # Add padding around the window

# Entry widget for user input
user_input = Entry(width=20)
user_input.grid(row=0, column=1, padx=10)

# Label next to input field
miles_label = Label(text="Miles", font=FONT)
miles_label.grid(row=0, column=2)

is_equal_label = Label(text="Is Equal to:", font=FONT) # Label for "Is Equal to:"
is_equal_label.grid(row=1, column=0, padx=10)

converter_label = Label(text=0, font=FONT) # Label to display conversion result
converter_label.grid(row=1, column=1)

km_label = Label(text="Km", font=FONT) # Label for "Km" unit
km_label.grid(row=1, column=2)

# Button to trigger conversion
calculate_button = Button(text="Calculate", font=FONT, command=converter)
calculate_button.grid(row=2, column=1, pady=10)

window.mainloop()