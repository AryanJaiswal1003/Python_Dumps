from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time


# ----------------------------
# SETTING UP THE GAME SCREEN
# ----------------------------
screen = Screen()
screen.setup(width=600, height=600) # Square screen
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(n=0) # Turn off auto-animation (manual update for smoothness)


# ----------------------------
# CREATE GAME OBJECTS
# ----------------------------
snake = Snake()  # Snake object (controls snake body and movement)
food = Food() # Food object (randomly appears on screen)
score = Score() # Scoreboard object (handles score + high score)


# ----------------------------
# KEYBOARD CONTROLS
# ----------------------------
screen.listen() # Start listening for key presses
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


# ----------------------------
# MAIN GAME LOOP
# ----------------------------
game_on = True
while game_on:
    screen.update() # Refresh the screen manually
    time.sleep(0.1) # Control the game speed
    snake.movement() # Move the snake forward

    # ------------------ DETECT COLLISION WITH FOOD ------------------
    if snake.head.distance(food) < 18:
        food.refresh() # Relocate food
        score.increase_score() # Update score
        snake.extend() # Add new segment to snake body

    # ------------------ DETECT COLLISION WITH WALL ------------------
    if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290:
        score.reset_score()  # Reset score & update high score if needed
        snake.reset_snake() # Reset snake to starting position

    # ------------------ DETECT COLLISION WITH TAIL ------------------
    # If snake's head collides with any of its body segments → reset

    for segment in snake.snake_body[1:]:  # Skip the head (index 0)
        if snake.head.distance(segment) < 10: # Head touching body segment
            score.reset_score()
            snake.reset_snake()

screen.exitonclick()