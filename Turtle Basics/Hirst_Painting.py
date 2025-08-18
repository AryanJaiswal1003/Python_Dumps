import random
from turtle import Turtle, Screen, colormode

""" EXTRACTS COLORS FROM THE IMG
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    new_color = (r, g, b)
    rgb_colors.append(new_color)"""

colormode(255) # Enable RGB color mode (0–255 range) so turtle can use RGB tuples

# Define a list of EXTRACTED RGB color tuples
colors = [
    (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
    (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165),
    (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129),
    (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)
]

tim = Turtle()
tim.width(20)  # Set pen width for dot size

tim.speed("fastest")
tim.hideturtle()

# Starting coordinates for the grid
x_coor = -240
y_coor = -240

for row in range(10): # Draw 10 rows of dots
    tim.penup()
    tim.setpos(x=x_coor, y=y_coor) # Move to start of current row
    tim.pendown()

    for _ in range(10): # Draw 10 dots in the current row
        tim.color(random.choice(colors))
        tim.dot(20) # Draw a dot with diameter 20
        tim.penup()
        tim.forward(50) # Space of 50 between 2 Dots
        tim.pendown()

    y_coor += 50 # Move up to start the next row

screen = Screen()
screen.exitonclick()