import random
from turtle import Turtle, Screen

# Create the screen and set up dimensions
screen = Screen()
screen.setup(width=500, height=400)

# Ask the user to place a bet on which turtle will win
user_bet = screen.textinput(
    title="Make Your Bet",
    prompt="Which Turtle will win the Race? Enter a Color:"
).title() # Convert input to Title Case to match color list

# List of turtle colors (6 players in the race)
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]

# Predefined y-coordinates so turtles line up evenly
y_coor = [-70, -40, -10, 20, 50, 80]

all_turtles = [] # Store all turtle racers in a list

# Create 6 turtles, assign colors, position them at the starting line
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x= -235, y= y_coor[turtle_index]) # Place turtle on starting line
    all_turtles.append(new_turtle) # Add turtle to the race list

# Flag to check if race should start
is_race_on = False
if user_bet: # If user entered a bet, race begins
    is_race_on = True

# Race loop
while is_race_on:
    for turtle in all_turtles:
        # Check if a turtle has crossed the finish line (x > 220)
        if turtle.xcor() > 220:
            winning_color = turtle.pencolor() # Get winning turtle's color
            # Compare winner with user's bet
            if winning_color == user_bet:
                print(f"You've Won!! The {winning_color} turtle is the Winner!!")
            else:
                print(f"You've Lost!! The {winning_color} turtle is the Winner..")

            is_race_on = False  # Stop the race

        # Move each turtle forward by a random distance (0–10)
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()