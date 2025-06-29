
# This file contains a function that prints a greeting message with the user's name.
# It prompts the user to enter their name and then displays a personalized welcome message.

def print_name(name):
    return f"\nHello, {name}! Welcome to my Website."

print_name("Ittani")  # Example usage, replace "User" with any name you want to test
def print_greeting():
    name = input("\nPlease enter your name: ")
    greeting = print_name(name)
    print(greeting)
# Example usage
if __name__ == "__main__":
    print_greeting()
    # You can call print_name directly with a name if you want to test it without user input
    # print(print_name("Ittani"))