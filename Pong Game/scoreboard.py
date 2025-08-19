from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

        self.l_score = 0 # Initialize left player's score
        self.r_score = 0 # Initialize right player's score

        self.update_scoreboard() # Display the initial scores

    # Update the scoreboard display with current scores
    def update_scoreboard(self):
        self.clear()

        # Position for left player's score
        self.goto(x=-100, y=190)
        self.write(arg=self.l_score, align="center", font=("Times New Roman", 50, "normal"))

        # Position for right player's score
        self.goto(x=100, y=190)
        self.write(arg=self.r_score, align="center", font=("Times New Roman", 50, "normal"))

    # Increment player's score and refresh display
    def l_point(self):
         self.l_score += 1
         self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()