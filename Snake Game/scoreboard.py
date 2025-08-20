from turtle import Turtle

# TODO - 6: CREATING SCOREBOARD & UPDATING THE SCORES
ALIGN = "center"
FONT = ("Times New Roman", 15, "normal")

class Score(Turtle):
    """Handles the scoreboard display, score updates, and high score tracking."""

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(x=0, y=270) # Position scoreboard at top of screen
        self.score = 0 # Instance variable for score

        # Open score.txt to fetch previously stored high score
        with open("score.txt") as high_score:
            self.high_score = int(high_score.read())

        self.update_score() # Display the initial scoreboard when the game starts


    def update_score(self):
        """Refresh the scoreboard with current score and high score."""
        self.clear()  # Remove old text before writing new one
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}",
                   align=ALIGN, font=FONT)


    def increase_score(self):
        """Increase the score by 1 point and refresh display."""
        self.score += 1
        self.update_score()

    # TODO: DETECT COLLISION WITH WALL & END THE GAME
    # def game_over(self):
    #     """Display 'Game Over' message in the center of the screen."""
    #     self.goto(x= 0, y= 0)
    #     self.write(arg="Game Over!!", align=ALIGN, font=FONT)

    def reset_score(self):
        """
        Reset the score after collision or game reset.
        - If current score is greater than stored high score, update the file.
        - Otherwise, just reset score to 0 and refresh scoreboard.
        """
        if self.score > self.high_score:
            with open("score.txt", mode="w") as stored_score:
                self.high_score = self.score
                stored_score.write(str(self.high_score))  # Save new high score
        self.score = 0 # Reset current score
        self.update_score() # Refresh display