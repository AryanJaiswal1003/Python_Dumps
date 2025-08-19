from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time


# SETTING UP THE GAME SCREEN
screen = Screen()
screen.setup(width=600, height=600) # Square screen
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(n=0) # Turn off auto-animation (manual update for smoothness)


# CREATE SNAKE, FOOD & SCOREBOARD OBJECTS
snake = Snake()
food = Food()
score = Score()


# Control the snake with keyboard keys
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


# ANIMATING THE SNAKE'S BODY
game_on = True
while game_on:
    screen.update() # Refresh the screen manually
    time.sleep(0.1) # Control the game speed
    snake.movement() # Move the snake forward

    # Detect collision with food
    if snake.head.distance(food) < 18:
        food.refresh() # Relocate food
        score.increase_score() # Update score
        snake.extend() # Add new segment to snake body

    # DETECT COLLISION WITH WALL & END THE GAME
    if (snake.head.xcor() > 290 or snake.head.ycor() > 290 or
            snake.head.xcor() < -290 or snake.head.ycor() < -290):
        score.game_over()
        game_on = False

    # TODO - 8: DETECT COLLISION WITH TAIL [IF HEAD COLLIDES WITH ANY SEGMENT IN TAIL THEN GAME END]
    for segment in snake.snake_body[1:]: # Exclude Head itself [USING PYTHON SLICING METHOD]
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()


screen.exitonclick()