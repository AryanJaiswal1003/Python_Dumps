## REEBORG'S WORLD

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Step 1: Find a wall first
while front_is_clear():
    move()
turn_left()

# Step 2: Apply right-hand rule
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()