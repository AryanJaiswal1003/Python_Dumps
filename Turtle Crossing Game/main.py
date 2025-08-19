import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# ---------------- SETUP THE SCREEN ---------------- #
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0) # Turn off automatic animation (manual updates)

# ---------------- CREATE GAME OBJECTS ---------------- #
player = Player() # The turtle controlled by player
car = CarManager() # Manages all cars
score = Scoreboard() # Displays current level / game over message

# ---------------- CONTROL BINDINGS ---------------- #
screen.listen()
screen.onkey(key="Up", fun=player.move)

# ---------------- GAME LOOP ---------------- #
game_is_on = True
while game_is_on:
    time.sleep(0.1)  # Slow down the loop (controls game speed)
    screen.update() # Refresh screen manually (because tracer(0) is set

    # Create new cars randomly and move all cars across the screen
    car.create_car()
    car.move_car()

    # ---------------- COLLISION DETECTION ---------------- #
    for each_car in car.all_cars:
        if each_car.distance(player) < 25: # If car is close to the player, game over
            score.game_over()
            game_is_on = False

    # ---------------- LEVEL UP ---------------- #
    if player.is_at_finish_line():
        player.go_to_start() # Reset player to bottom
        car.increment_speed() # Make cars faster
        score.increase_level() # Update scoreboard

screen.exitonclick()