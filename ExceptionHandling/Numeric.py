# Try function to handle exceptions in numeric operations

try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("Invalid input! Please enter a valid integer.")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")
else:
    # This block executes if no exceptions were raised
    print(f"The result of 10 divided by {number} is {result}")

print("The program terminated successfully.")
print("End of numeric operations.")


# This is for exception handling in the numeric operations module
