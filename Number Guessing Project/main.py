import random
from art import logo

ORIGINAL_NUM = random.randint(1, 100)
lives = None

def attempts():
    global lives

    # Welcome message and difficulty selection
    print(logo)
    print("Welcome to the Number Guessing Game!! 😎\nI'm Thinking of a Number between 1 and 100.\n")
    user_choice = input("Choose Difficulty Level [Easy / Hard]: ").lower()

    # Set number of lives based on difficulty
    if user_choice == "easy":
        lives = 10
    elif user_choice == "hard":
        lives = 5
    else:
        print("You have Entered a Wrong Input")
        return


def play_game():
    global lives
    attempts() # Calls attempts() to set up the game and difficulty level
    
    game_over = False
    while not game_over:
        user_input = int(input("Make a Guess: ")) # Get user's guess

        if abs(user_input - ORIGINAL_NUM) == 2: # Check if guess is very close (+/- 2) to the original number
            lives -= 1
            print(f"Your guess {user_input} is very close to the number!\nGuess Again ??\n")

        elif user_input < ORIGINAL_NUM: # Check if guess is too low
            lives -= 1
            print(f"Number Guessed {user_input} is Too Low.\nGuess Again 😂\n")

        elif user_input > ORIGINAL_NUM: # Check if guess is too high
            lives -= 1
            print(f"Number Guessed {user_input} is Too High.\nGuess Again 😉\n")

        else: # Check if guess is correct
            print(f"The Number Guessed {user_input} is Correct.. You Win 😎\n")
            game_over = True
            continue

        print(f"You have {lives} Attempts Remaining to Guess the Number.\n") # Show remaining attempts

        # End game if out of lives
        if lives == 0:
            print(f"You've run out of attempts. The number was {ORIGINAL_NUM}. You lose 🤣🤯\nRefresh the Game to Play Again\n")
            game_over = True

    # Ask user if they want to play again
    play_again = input("Do you want to play again? (Y/N): ").lower()
    if play_again == "y":
        print("\n" * 20)
        play_game()

play_game()