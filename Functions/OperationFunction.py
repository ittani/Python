# creating function for practicing


def add(x, y):
    """
    This function adds two numbers.
    :param x: First number
    :param y: Second number
    :return: Sum of x and y
    """
    return x + y

def subtract(x, y):
    """
    This function subtracts the second number from the first.
    :param x: First number
    :param y: Second number
    :return: Difference of x and y
    """
    return x - y

def multiply(x, y):
    """
    This function multiplies two numbers.
    :param x: First number
    :param y: Second number
    :return: Product of x and y
    """
    return x * y

operation = input("\nChoose an operation (add, subtract, multiply): ").strip().lower()

# Validate the operation input
if operation not in ['add', 'subtract', 'multiply']:
    print("Invalid operation. Please choose from add, subtract, or multiply.")
    exit() 
elif operation == 'add':
    print("You chose addition.")
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        exit()
    print("Result:", add(x, y)) if 'x' in locals() and 'y' in locals() else None
elif operation == 'subtract':
    print("You chose subtraction.")
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        exit()
    print("Result:", subtract(x, y)) if 'x' in locals() and 'y' in locals() else None
elif operation == 'multiply':
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        exit()
    # Perform multiplication
    print("You chose multiplication.") 
    print("Result:", multiply(x, y)) if 'x' in locals() and 'y' in locals() else None
# Prompting user for input
print("....The End of the Function6....")
  
# This code defines three functions for basic arithmetic operations: addition, subtraction, and multiplication.
# It prompts the user to input two numbers, performs the operations, and prints the results.        