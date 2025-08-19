from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, coordinates):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()

        self.shapesize(stretch_len=1, stretch_wid=5) # Stretch the square vertically to form a paddle
        self.goto(coordinates) # Position the paddle at the given coordinates

    # TODO: MOVING PADDLE
    def up_movt(self):
        new_y = self.ycor() + 20 # Calculate new y-coordinate
        self.goto(x=self.xcor(), y=new_y)

    def down_movt(self):
        new_y = self.ycor() - 20 # Calculate new y-coordinate
        self.goto(x=self.xcor(), y=new_y)