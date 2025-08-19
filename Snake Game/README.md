## Snake Game (OOP Version)

This is a classic Snake Game built using Python’s Turtle Graphics module and Object-Oriented Programming concepts.

--- 

## The project is modularized into multiple classes:

    * Snake → Handles the snake’s body, movement, and direction.
    * Food → Represents the food the snake eats.
    * Scoreboard → Displays and updates the score.
    * Main → The entry point that ties everything together.

---

## Game Rules

    * Use the arrow keys (↑ ↓ ← →) to control the snake --> Eat the food 🐢 to grow longer and score points.

    * The game ends if: The snake hits the wall **OR** The snake collides with its own tail.

---

## Project Structure
📂 Snake_Game
 
    📜 main.py         # Main game loop & controls
    📜 snake.py        # Snake class (movement & body handling)
    📜 food.py         # Food class (randomly placed food)
    📜 scoreboard.py   # Scoreboard class (score display & game over)
    📜 README.md       # Documentation

---

## Concepts Used

1. Encapsulation: Each class (Snake, Food, Score) handles its own behavior.
2. Abstraction: Complex logic (movement, score update, food spawning) is hidden inside methods.
3. Reusability: Separate files and classes make it easy to extend features.
4. Modularity: Clear separation of game components.

5. Slicing: Extracting a portion (subsequence) of a list, tuple, string, or any sequence type --> [start:end:step].

