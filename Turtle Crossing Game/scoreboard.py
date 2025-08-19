from turtle import Turtle

# Constant values for text styling
FONT = ("Times New Roman", 24, "normal")
ALIGN = "left"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        """Initialize the scoreboard as a Hidden Turtle object."""
        self.color("black")
        self.penup()
        self.hideturtle()
        self.setposition(x=-285, y=250)
        self.level = 1 # Start level
        self.update_level() # Display the initial level


    def update_level(self):
        """Clear old text and rewrite the current level on screen."""
        self.clear()  # Remove previous text
        self.write(arg=f"Level: {self.level}", align=ALIGN, font=FONT)


    def increase_level(self):
        """Increase level by 1 and refresh the scoreboard display."""
        self.level += 1
        self.update_level()


    # TODO: DETECT COLLISION WITH CAR & END THE GAME
    def game_over(self):
        """Display 'Game Over' message in the center of the screen."""
        self.goto(x= 0, y= 0)
        self.write(arg="Game Over!!", align=ALIGN, font=FONT)