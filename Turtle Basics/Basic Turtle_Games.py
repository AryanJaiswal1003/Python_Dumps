import random
import turtle
from turtle import Turtle,Screen

tim = Turtle()
tim.hideturtle()

turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    colors = (r, g, b)
    return colors


# TODO-1: CODE FOR POLYGON GENERATOR
sides = 3 # Start with a triangle

# Loop to draw polygons from 3 to 10 sides
while sides <= 10:
    angle = 360 / sides # Calculate internal angle for the polygon
    tim.pencolor(random_color())

    for _ in range(sides): # Draw the current polygon
        tim.forward(100)
        tim.right(angle=angle) # Turn right by calculated angle

    sides += 1 # Move to the next polygon (increase number of sides)



# TODO-2: CODE FOR TURTLE RANDOM WALK
angle = [0, 90, 180, 270]  # Define possible movement directions (in degrees) [Right, Up, Left, Down]

# Set turtle appearance and speed
tim.pensize(width=15)
tim.speed('fastest')

# Perform 200 steps of random movement
for _ in range(200):
    tim.color(random_color())
    tim.setheading(to_angle=random.choice(angle)) # Face a random cardinal direction
    tim.forward(30)



# TODO-3: CODE FOR SPIROGRAPH
for _ in range(180): # 360° / 2° = 180 iterations
    tim.color(random_color())
    tim.circle(100) # Draw a circle with radius 100
    tim.right(2)  # Rotate the turtle 2° to the right


screen = Screen()
screen.mainloop()