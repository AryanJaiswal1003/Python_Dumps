from paddle import Paddle
from turtle import Screen
from ball import Ball
from scoreboard import Scoreboard
import time

# -------------------- SETUP GAME SCREEN --------------------
screen = Screen()
screen.setup(width=800, height=600)  # Set screen size
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0) # Turn off automatic screen updates (we'll update manually)

# -------------------- CREATE GAME OBJECTS --------------------
r_paddle = Paddle((350, 0)) # Right paddle at x=350
l_paddle = Paddle((-350, 0)) # Left paddle at x=-350
ball = Ball() # Create the ball
scoreboard = Scoreboard() # Create the scoreboard

# -------------------- KEY BINDINGS --------------------
screen.listen()
screen.onkey(key="Up", fun=r_paddle.up_movt)
screen.onkey(key="Down", fun=r_paddle.down_movt)
screen.onkey(key="w", fun=l_paddle.up_movt)
screen.onkey(key="s", fun=l_paddle.down_movt)

# -------------------- MAIN GAME LOOP --------------------
is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed) # Control ball speed
    screen.update() # Refresh screen after movements
    ball.move() # Move ball forward

    # -------------------- BALL COLLISION WITH WALLS --------------------
    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.bounce_y() # Reverse vertical direction


    # -------------------- BALL COLLISION WITH PADDLES --------------------
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320 or
            ball.distance(l_paddle) < 50 and ball.xcor() < - 320):
        ball.bounce_x() # Reverse horizontal direction


    # -------------------- RIGHT WALL: PLAYER 1 SCORES --------------------
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_point()

    # -------------------- LEFT WALL: PLAYER 2 SCORES --------------------
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_point()

screen.exitonclick()