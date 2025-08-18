from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
screen = Screen()

# --- Movement Functions ---
def move_forward():
    tim.forward(20)


def move_backward():
    tim.backward(20)


def move_left():
    """Rotate the turtle 10° to the left (counterclockwise)"""
    tim.left(angle=10)


def move_right():
    """Rotate the turtle 10° to the right (clockwise)"""
    tim.right(angle=10)


def screen_clear():
    """Clear the drawing and reset turtle to center"""
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


# --- Key Bindings ---
screen.listen() # Start listening for keyboard events
screen.onkey(key="Up", fun=move_forward)
screen.onkey(key="Left", fun=move_left)
screen.onkey(key="Right", fun=move_right)
screen.onkey(key="Down", fun=move_backward)
screen.onkey(key="space", fun=screen_clear)

screen.exitonclick()