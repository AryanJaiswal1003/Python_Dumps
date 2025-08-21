from turtle import Turtle, Screen
import pandas

# Constants for text formatting
ALIGN = "center"
FONT = ("Times New Roman", 8, "normal")

image = "blank_states_img.gif" # Load the background image of the U.S. map

data =  pandas.read_csv("50_states.csv") # Read the CSV file containing all states and their coordinates
all_states = data["state"].tolist() # Convert states column to a Python list

# Setup the screen
screen = Screen()
screen.title("U.S. States Game")
screen.addshape(image) # Register the map image as a turtle shape

# Create a turtle to display the background map
main = Turtle()
main.shape(image)

# Create a turtle for writing state names on the map
writer = Turtle()
writer.hideturtle()
writer.penup()

"""
Optional: Function to get coordinates by clicking on the map. Helps in debugging or creating your own CSV file with positions

def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)
"""

guessed_state = [] # List to keep track of correctly guessed states

while len(guessed_state) < 50: # Game loop → keep running until all 50 states are guessed

    # Prompt the user to guess a state
    user_input = screen.textinput(
        title=f"{len(guessed_state)} / 50 States Correct",
        prompt="Guess What's the Next State?"
    ).title() # Convert input to Title Case for matching

    if user_input in all_states and user_input not in guessed_state: # If the guess is valid (exists in dataset & not guessed before)
        # Retrieve the (x, y) coordinates of the guessed state from the dataset
        state_data = data[data.state == user_input]
        x_coor = state_data['x'].item()
        y_coor = state_data['y'].item()

        # Move the writer turtle to the location and write the state name
        writer.goto(x= x_coor, y=y_coor)
        writer.write(arg=user_input, align=ALIGN, font=FONT)

        guessed_state.append(user_input) # Add the state to the guessed list


screen.mainloop()