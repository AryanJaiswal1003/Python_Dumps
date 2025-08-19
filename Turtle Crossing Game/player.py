from turtle import Turtle

# Constants for player behavior and positioning
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280  # Y-coordinate for reaching the finish line (top of screen)


class Player(Turtle):

    def __init__(self):
        super().__init__()
        """Initialize the player (turtle) and place it at the starting position."""
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(to_angle=90) # Make turtle face upwards (north)

    def move(self):
        """Move the turtle forward by a fixed distance."""
        self.forward(distance=MOVE_DISTANCE)

    def is_at_finish_line(self):
        """Check if player has crossed the finish line (reached top)."""
        if self.ycor() > FINISH_LINE_Y: # Compare current y-position with finish line
            return True
        else:
            return False

    def go_to_start(self):
        """Reset player back to the starting position."""
        self.goto(STARTING_POSITION)