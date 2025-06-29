# Built in functions are functions that are always available in Python. They are part of the Python language and do not require any imports to use. Here are some commonly used built-in functions:
# 1. `print()`: Outputs data to the console.
# 2. `len()`: Returns the length of an object (e.g., string, list).
# 3. `type()`: Returns the type of an object.
# 4. `int()`: Converts a value to an integer.
# 5. `str()`: Converts a value to a string.
# 6. `list()`: Converts a value to a list.
# 7. `dict()`: Creates a dictionary.
# 8. `set()`: Creates a set.    

message = "I am a built-in function in Python. I can be used to perform various tasks without needing to import any modules."
print(message)
print(message.upper())  # Converts the message to uppercase
print(message.lower())  # Converts the message to lowercase
print(message.title())  # Converts the message to title case
print(message.split())  # Splits the message into a list of words
print(message.replace("Python", "programming"))  # Replaces "Python" with "programming"
print(len(message))  # Returns the length of the message
print(type(message))  # Returns the type of the message
print(message.find("built-in"))  # Finds the index of the substring "built-in"


# Example of using a built-in function to check if a number is even or odd
def is_even(num):
    """Check if a number is even."""
    return num % 2 == 0
print("\n",is_even(30))  # True
print(is_even(23))   # False

# Example of using a built-in function to find the maximum value in a list
def find_max(numbers):
    """Find the maximum value in a list."""
    return max(numbers)
print("\n",find_max([-100, 234, 390, 927, 599]))  
print(find_max([10, 20, 30, 40, 50]))     

# Joining strings using a built-in function
def join_strings(strings, separator="."):
    """Join a list of strings with a specified separator."""
    return separator.join(strings)
print("\n",join_strings(["192", "168", "49","12"]))
print("\n",join_strings(["192", "164", "32","5"]))