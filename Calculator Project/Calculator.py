from art import logo
print(logo)

# TODO: CREATING THE MATHEMATICAL FUNCTIONS [ADD, SUBTRACT, MULTIPLY, DIVIDE]
def add(n1, n2):
    return n1 + n2

def subtract(n1 , n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO: ADD THESE 4 FUNCTIONS INTO A DICTIONARY AS THE VALUES. KEYS = "+", "-", "*", "/"
maths_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
# TODO: USE THE DICTIONARY OPERATIONS TO PERFORM THE CALCULATIONS.

# Control variable for the main calculator loop
will_continue = True
num1 = None  # Used to store the first number or previous result

while will_continue:

    if num1 is None: # Prompt for first number only if starting fresh
        num1 = float(input("Enter your First Number: "))

    # Ask user for operator and second number
    operator = input("Choose the Operator you want to Perform ['+', '-', '*', '/']: ")
    num2 = float(input("Enter your Second Number: "))

    if operator in maths_dict: # Perform calculation if operator is valid
        result = maths_dict[operator](num1, num2)
        print(f"Result: [{num1} {operator} {num2}] --> {result}")
    else:
        print("Invalid operator. Please choose from '+', '-', '*', '/'.")
        continue  # Skip to next iteration if operator is invalid

    # Ask user if they want to continue with the result or start fresh
    user_choice = input("Type 'Yes' to Continue & Type 'No' to Start Fresh: ").lower()
    if user_choice == 'no':
        print("\n" * 100)
        print(logo)
        num1 = None # Reset num1 to start a new calculation
    else:
        num1 = result # Use previous result as new num1 for next calculation