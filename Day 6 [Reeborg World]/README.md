## Reeborg's World – Maze Solver

This script solves the **Maze** world in [Reeborg's World](https://reeborg.ca) using the **right-hand rule**.  
It first ensures the robot is aligned against a wall to avoid infinite loops when starting in open space.

## Algorithm Steps
1. Find the wall
    --> Move forward until a wall is encountered.
    --> Turn left to prepare for wall-following.
4. Right-hand rule
    --> If right is clear → turn right, move.
    --> Else if front is clear → move forward.
    --> Else → turn left.

## Notes: 
--> Works on any maze solvable by the right-hand wall-following method.
--> Prevents infinite looping in open areas by first aligning to a wall.