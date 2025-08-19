from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

        self.x_move = 10 # Initial horizontal movement increment
        self.y_move = 10 # Initial vertical movement increment

        self.move_speed = 0.1 # Initial speed of the ball (used with time.sleep)


    def move(self): # Update ball position based on current movement increments
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)


    def bounce_y(self): # Reverse vertical direction when hitting top/bottom walls
        self.y_move *= - 1

    def bounce_x(self): # Reverse horizontal direction when hitting paddles
        self.x_move *= -1
        self.move_speed *= 0.9 # Also increase speed slightly to make the game harder


    def reset_ball(self): # Reset ball to center after a point is scored
        self.goto(x=0, y=0)
        self.move_speed = 0.1 # Reset speed to default
        self.bounce_x()  # Reverse direction to serve toward scorer