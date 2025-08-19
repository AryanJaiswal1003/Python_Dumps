from turtle import Turtle
import random

# Constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        """Initialize car manager with an empty list of cars and base speed."""
        self.all_cars = [] # Stores all car objects
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        """Randomly create a new car and place it on the right side of the screen."""
        random_chance = random.randint(1, 6) # 1 in 6 chance (controls car frequency)

        if random_chance == 6:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1) # Stretch to rectangle
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250) # Random vertical position
            new_car.goto(x=300, y=random_y) # Start on right side of screen
            self.all_cars.append(new_car)


    def move_car(self):
        """Move all cars leftwards across the screen based on current speed."""
        for car in self.all_cars:
            car.backward(self.car_speed) # Move towards left (negative x-direction)


    def increment_speed(self):
        """Increase car speed when the player levels up."""
        self.car_speed += MOVE_INCREMENT