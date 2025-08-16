# Import necessary classes from respective modules
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Initialize instances of Menu, CoffeeMaker, and MoneyMachine
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# Flag to control the main loop; False means the machine is running
is_on = False
while not is_on:
    user_input = input("What do you want to have Today? [Espresso / Latte / Cappuccino]: ").lower() # Prompt user for their drink choice

    # Check if input matches any available menu item
    if user_input in menu.get_items():
        ordered = menu.find_drink(order_name=user_input) # Retrieve the drink object from the menu

        # Check if resources are sufficient & payment is successful
        if coffee_maker.is_resource_sufficient(drink=ordered) and money_machine.make_payment(cost=ordered.cost):
                coffee_maker.make_coffee(order=ordered)

    # If user requests a report, print current resource status
    if user_input == 'report':
        coffee_maker.report()
        money_machine.report()

    # If user enters 'off', terminate the loop and shut down the machine
    if user_input == 'off':
        is_on = True
