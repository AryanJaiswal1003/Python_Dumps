from art import logo, vs
from game_data import data
import random

score = 0
used_ques = [] # List to track already used comparisons

# Select the first comparison item randomly
compare = random.choice(data)
used_ques.append(compare) # Mark it as used

game_over = False
while not game_over:
    # Filter out already used questions to avoid repetition
    available_ques = [item for item in data if item not in used_ques]

    if not available_ques: # If no unique questions left, end the game
        print("No Unique Questions Left.. Game Over!!")
        break

    against = random.choice(available_ques) # Select a new item to compare against
    used_ques.append(against) # Mark it as used

    # Extract follower counts for comparison
    compare_followers = compare['follower_count']
    against_followers = against['follower_count']

    print(logo)
    if score > 0: # Show score only after the first correct answer
        print(f"You're Right! Current score: {score}")

    # Display comparison details
    print(f"Compare A: {compare['name']}, a {compare['description']}, from {compare['country']}.")
    print(vs)
    print(f"Against B: {against['name']}, a {against['description']}, from {against['country']}.\n")


    user_input = input("Who has More Followers? Type 'A' or 'B': ").lower()
    if (user_input == 'a' and compare_followers >= against_followers) or \
            (user_input == 'b' and against_followers >= compare_followers):
        score += 1
        compare = against # Move to next round with new comparison

    else:
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True