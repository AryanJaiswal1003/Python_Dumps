# TODO - 3: CREATING A SNAKE CLASS & MOVE ALL FUNCTIONALITIES USING OOP CONCEPTS
from turtle import Turtle
COORDINATES = [(0, 0), (-20, 0), (-40, 0)] # Initial positions for the snake segments
MOVE_DISTANCE = 20

# Direction constants (in degrees)
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        """Initialize the snake with its body and head"""
        self.snake_body = []
        self.create_body()  # Create the initial 3-segment snake
        self.head = self.snake_body[0] # Define the first segment as the head


    # TODO - 1: CREATING THE SNAKE'S BODY [Converted to OOP]
    def create_body(self):
        """Creates the snake's body using predefined coordinates"""
        for position in COORDINATES:
            self.add_segment(position) # Add one segment for each coordinate

    def add_segment(self, position):
        """Add a single segment at a given position"""
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.snake_body.append(segment)  # Adds new segment to the snake_body list


    def extend(self):
        """Add a new segment to the end of the snake (when it eats food)"""
        self.add_segment(self.snake_body[-1].position()) # Adds a new segment at the same position as the last segment


    # TODO - 2: ANIMATING THE SNAKE'S BODY [Converted to OOP]
    def movement(self):
        """Moves the snake forward by shifting segments to follow the head"""
        # Move each segment to the position of the one ahead of it
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE) # Move the head forward in the current heading direction


    # TODO - 4: CONTROLLING THE SNAKE WITH THE KEYPRESS
    def up(self):
        """Turn snake upward if not currently moving down"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Turn snake downward if not currently moving up"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Turn snake left if not currently moving right"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Turn snake right if not currently moving left"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)