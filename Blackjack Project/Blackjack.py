import random
from art import logo

# Function to deal a Random card from the Deck
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# Function to Calculate the Score of a Hand
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2: # Check for Blackjack (Ace + 10-value card)
        return 0

    if sum(cards) > 21 and 11 in cards: # Adjust Ace value if score goes over 21
        cards.remove(11)
        cards.append(1)

    return sum(cards)

# Function to compare user and computer Scores & Return the Result
def compare(u_score, c_score):
    if u_score == c_score:
        return "Its a Draw 👌🔥"
    elif c_score == 0:
        return "Opponent Score's a Blackjack.. Computer Wins 🧛‍♂️😎"
    elif u_score == 0:
        return "You Score a Blackjack.. You Win 🤦‍♂️😍"
    elif u_score > 21:
        return "You Went Over.. You Loose 🤣👌"
    elif c_score > 21:
        return "Your Opponent Went Over.. You Win 😉🥲"
    elif u_score > c_score:
        return "You Win.. 😭🤯"
    else:
        return "Your Opponent Win.. 😂😉"

# Main Game Loop: Runs as long as the user wants to play
while input("Do you want to Play a Game of Blackjack? Type 'Y' or 'N': ").lower() == "y":
    print("\n" * 20) # Clear the screen
    print(logo) # Display game logo

    # Initialize hands for user and computer
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    game_over = False
    computer_score = -1
    user_score = -1

    # User's Turn
    while not game_over:
        user_score = calculate_score(cards = user_cards)
        computer_score = calculate_score(cards = computer_cards)
        print(f"Your Cards: {user_cards}, Current Score: {user_score}")
        print(f"Computer's First Card: {computer_cards[0]}")

        # Check for game-ending conditions
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_input = input("Type 'Y' to get Another Card, Type 'N' to Pass: ").lower()
            print("\n" * 2)

            if user_input == 'y':
                print("\n")
                user_cards.append(deal_card()) # User draws another card
            elif user_input == 'n':
                game_over = True
            else:
                print("You have Entered a Wrong Input")

    # Computer's turn: draws cards until score is 17 or higher, unless it has Blackjack
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(cards = computer_cards)
        print("\n")
        
    # Show final hands and scores, then display result
    print(f"Your Final Hand: {user_cards}, Final Score: {user_score}")
    print(f"Computer's Final Hand: {computer_cards}, Final Score: {computer_score}")
    print(compare(u_score=user_score, c_score=computer_score))