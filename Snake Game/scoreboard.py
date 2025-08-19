from turtle import Turtle

# TODO - 6: CREATING SCOREBOARD & UPDATING THE SCORES
ALIGN = "center"
FONT = ("Times New Roman", 15, "normal")

class Score(Turtle):
    """Handles the scoreboard display and score updates."""

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(x=0, y=270) # Position scoreboard at top of screen

        self.score = 0 # Instance variable for score
        self.update_score() # Display starting score


    def update_score(self):
        """Refresh the scoreboard text with current score"""
        self.clear()  # Remove previous text
        self.write(arg=f"Score: {self.score}", align=ALIGN, font=FONT)


    def increase_score(self):
        """Increase score by 1 and update the display."""
        self.score += 1
        self.update_score()

    # TODO - 7: DETECT COLLISION WITH WALL & END THE GAME
    def game_over(self):
        """Display 'Game Over' message in the center of the screen."""
        self.goto(x= 0, y= 0)
        self.write(arg="Game Over!!", align=ALIGN, font=FONT)