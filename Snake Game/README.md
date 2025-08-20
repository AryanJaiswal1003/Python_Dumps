## Snake Game (OOP Version)

This is a classic Snake Game built using Python’s Turtle Graphics module and Object-Oriented Programming concepts.

--- 

## The project is modularized into multiple classes:

    * Snake Movement – Control the snake using arrow keys (Up, Down, Left, Right).
    * Food Generation – Food appears at random positions; eating food grows the snake.
    * Scoreboard – Tracks current score and displays High Score across sessions.
    * Collision with Wall – If the snake hits the wall, the game resets but keeps high score.
    * Collision with Tail – If the snake collides with its own body, the game resets.
    * High Score Persistence – High score is saved in a file (score.txt) so it remains even after the game is closed.

---

## Game Rules

    * Use the arrow keys (↑ ↓ ← →) to control the snake --> Eat the food 🐢 to grow longer and score points.
    * The game resets if: The snake hits the wall **OR** The snake collides with its own tail.

---

## Project Structure
    snake_game/
    ├── main.py          # Main game loop (screen, controls, collisions)
    ├── snake.py         # Snake class (movement, growth, reset)
    ├── food.py          # Food class (random spawning)
    ├── scoreboard.py    # Scoreboard class (current score + high score tracking)
    ├── score.txt        # Stores high score persistently

---

## Concepts Used

    1. Encapsulation: Each class (Snake, Food, Score) handles its own behavior.
    2. Abstraction: Complex logic (movement, score update, food spawning) is hidden inside methods.
    3. Reusability: Separate files and classes make it easy to extend features.
    4. Modularity: Clear separation of game components.
    5. Slicing: Extracting a portion (subsequence) of a list, tuple, string, or any sequence type --> [start:end:step].

---