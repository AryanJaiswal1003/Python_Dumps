from ingredients import MENU, resources
from logo import image

# Initialize global resource and money variables
WATER = resources['water']
MILK = resources['milk']
COFFEE = resources['coffee']
MONEY = 0 # Total money collected from successful transactions

# Function to handle coin input and payment processing
def process_money(order):
    print("\nPlease Insert Coins.")
    cost = MENU[order]['cost'] # Get the cost of the selected drink

    # Ask user for number of each coin type
    quarters = int(input("How Many Quarters?: "))
    dimes = int(input("How Many Dimes?: "))
    nickles = int(input("How Many Nickles?: "))
    pennies = int(input("How Many Pennies?: "))

    # Calculate total money inserted
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

    if total >= cost: # Check if payment is sufficient
        change = round(total - cost, 2)
        if change > 0:
            print(f"\nHere is ${change} in Change.")
        return cost # Return the amount to be added to MONEY
    else:
        print(f"\nSorry that's Enough Money. Money ${total} Refunded.")
        return None # Transaction failed


# Function to check resources and process drink order
def materials(choice):
    global WATER, MILK, COFFEE, MONEY

    # Show current resource and money status
    if choice == 'report':
        print(f"Total Water: {WATER}ml\nTotal Milk: {MILK}ml\nTotal Coffee: {COFFEE}g\nMoney: ${MONEY}")
        return

    # Handle invalid drink choices
    if choice not in MENU:
        print("Invalid Choice. Please select Espresso, Latte, or Cappuccino.")
        return

    # Get required ingredients for the selected drink
    ingredients = MENU[choice]['ingredients']
    req_water = ingredients.get('water', 0)
    req_coffee = ingredients.get('coffee', 0)
    req_milk = ingredients.get('milk', 0)

    # Check if enough resources are available
    if WATER >= req_water and MILK >= req_milk and COFFEE >= req_coffee:
        money_paid = process_money(order=choice) # Process payment

        # Deduct ingredients and update money
        if money_paid is not None:
            MONEY += money_paid
            WATER -= req_water
            MILK -= req_milk
            COFFEE -= req_coffee
            print(f"Here is your {choice}🍵☕.. Enjoy!!\n")
    else:
        print(f"Sorry there is Not Enough Ingredients to Make {choice}..\n")


# Main loop to keep the machine running until user turns it off
game_over = False
while not game_over:
    print("\n" * 20)
    print(image)
    user_input = input("What would you Like to Have? [Espresso/Latte/Cappuccino]: ").lower()

    if user_input == 'off': # Exit condition
        game_over = True
    else:
        materials(choice=user_input) # Process the user's choice