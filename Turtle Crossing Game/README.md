## Turtle Crossing Game

A fun arcade-style game built with Python’s Turtle graphics module, inspired by the classic Frogger. The goal is simple:
➡ Help the turtle cross the road while avoiding speeding cars! & Each time the turtle reaches the top, the level increases 
    and cars move faster.

---

## Game Rules

    * The turtle starts at the bottom of the screen.
    * Press the Up arrow key ⬆️ to move forward.
    * Cars spawn randomly from the right and drive left across the screen.
    * If the turtle collides with a car → Game Over ❌
    * If the turtle reaches the finish line (top):
        --> The level & Car speed increases.
        --> Turtle resets to the starting position.

---

## Project Structure

    turtle-crossing/
    │── main.py           # Main game loop
    │── player.py         # Player (turtle) class
    │── car_manager.py    # Handles car creation, movement & speed
    │── scoreboard.py     # Displays level and Game Over message
    │── README.md         # Project documentation

---