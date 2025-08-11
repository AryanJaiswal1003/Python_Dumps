from art import logo
print(logo)

# Function to find and print the highest bidder
def highest_bidder(bids):
    winner = ""
    highest_bid = 0

    # Iterate through all bids to find the highest
    for key in bids:
        bid_amount = bids[key]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = key

    print(f"The Winner is {winner} with Bid of Rs. {highest_bid}") # Print the winner and their bid

# ************************************************ [OTHER WAY] ************************************************
# max_value = 0
# max_key = ""
# for key, value in bid_game.items():
#     if value > max_value:
#         max_key = key
#         max_value = value
# print(f"The Winner is {max_key} with Bid of Rs. {max_value}")
# -------------------------------------------------------------------------------------------------------------


user_details = {} # Dictionary to store user_names and their bids
should_continue = True

while should_continue:

    user_name = input("What is Your Name?: ").lower()
    user_bid = int(input("Enter your Bid Amount: $ "))

    # Store the bid in the dictionary
    user_details[user_name] = user_bid  # Fixed assignment operator

    decision = input("Are there any other bidders? Type 'yes or 'no'.\n").lower() # Ask if there are more bidders

    if decision == 'no':
        should_continue = False # If no more bidders, end loop and announce winner
        highest_bidder(bids=user_details)
    else:
        print("\n" * 100)  # Clear the screen for the next bidder (simulated)