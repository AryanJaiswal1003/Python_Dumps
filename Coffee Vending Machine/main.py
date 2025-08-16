from ingredients import MENU, resources
from logo import image

# Initialize global resource and money variables
MONEY = 0 # Total money collected from successful transactions

# Function to check if resources are sufficient for the selected drink
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f"Sorry there is not enough {item}.\n")
            return False
    return True

# Function to handle coin input and payment processing
def process_money(order):
    print("\nPlease Insert Coins.")
    cost = MENU[order]['cost'] # Get the cost of the selected drink

    # Ask user for number of each coin type
    try:
        quarters = int(input("How Many Quarters?: "))
        dimes = int(input("How Many Dimes?: "))
        nickles = int(input("How Many Nickles?: "))
        pennies = int(input("How Many Pennies?: "))
    except ValueError:
        print("Invalid input. Please enter whole numbers for coins.")
        return None

    # Calculate total money inserted
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

    if total >= cost: # Check if payment is sufficient
        change = round(total - cost, 2)
        print(f"\nHere is ${change} in Change.")
        return cost # Return the amount to be added to MONEY
    else:
        print(f"\nSorry that's Enough Money. Money ${total} Refunded.")
        return None # Transaction failed


# Function to check resources and process drink order
def materials(choice):
    global MONEY
    # Show current resource and money status
    if choice == 'report':
        print(f"Total Water: {resources['water']}ml\n"
              f"Total Milk: {resources['milk']}ml\n"
              f"Total Coffee: {resources['coffee']}g\n"
              f"Money: ${MONEY}")
        return

    # Handle invalid drink choices
    if choice not in MENU:
        print("Invalid Choice. Please select Espresso, Latte, or Cappuccino.")
        return
        
    ingredients = MENU[choice]['ingredients'] # Get required ingredients for the selected drink

    if is_resource_sufficient(order_ingredients=ingredients): # Check if enough resources are available
        money_paid = process_money(order=choice) # Process payment

        if money_paid is not None: # Deduct ingredients and update money
            MONEY += money_paid
            for item in ingredients:
                resources[item] -= ingredients[item]
            print(f"Here is your {choice}🍵☕.. Enjoy!!")


# Main loop to keep the machine running until user turns it off
game_over = False
while not game_over:
    user_input = input("What would you Like to Have? [Espresso/Latte/Cappuccino]: ").lower()
    if user_input == 'off': # Exit condition
        game_over = True
    else:
        materials(choice=user_input) # Process the user's choice
