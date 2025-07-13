# Looping Exception Handling Example

class LoopException(Exception):
    """Exception raised for errors in the loop processing."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def process_numbers(numbers):
    """Process a list of numbers, handling exceptions."""
    results = []
    for number in numbers:
        try:
            if not isinstance(number, int):
                raise ValueError("Only integers are allowed.")
            if number == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            result = 10 / number
            results.append(result)
        except ValueError as ve:
            print(f"ValueError: {ve}")
        except ZeroDivisionError as zde:
            print(f"ZeroDivisionError: {zde}")
        except LoopException as le:
            print(f"LoopException: {le.message}")
    return results

# Example usage:
if __name__ == "__main__":  
    numbers = [2, 0, 'a', 5, 10]
    results = process_numbers(numbers)
    print("Processed results:", results)  # Output: Processed results: [5.0, 2.0] (ignoring errors)
    print("End of loop processing.")