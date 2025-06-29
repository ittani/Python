
""""
We gonna do fun stuff with loops
"""

# Infinite loop example
# This code will run indefinitely until interrupted by the user (e.g., pressing Ctrl+C)
# It prints a message every second and doubles the value of x each time
# The loop will break when x reaches or exceeds 250
import time
import sys

print("\n\nLet's do some fun stuff with loops!\n")
print("This code will run indefinitely until you stop it with Ctrl+C.\n")   
# Importing necessary libraries
# time for sleep functionality and sys for output control
# ANSI color codes
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

x = 2
frame = ["|", "/", "-", "\\"]

print(f"{YELLOW}🚀 Starting the loop... Press Ctrl+C to escape! 🧠{RESET}\n")

try:
    while True:
        for symbol in frame:
            sys.stdout.write(f"\r{GREEN}🤖 Waiting for you to press Ctrl+C: {x} {symbol}{RESET}")
            sys.stdout.flush()
            time.sleep(0.2)

        x *= 2
        if x >= 10000:
            print(f"\n\n{RED}🔥 x has reached {x}. Exiting the loop in style! 💥{RESET}")
            break

except KeyboardInterrupt:
    print(f"\n\n{YELLOW}🛑 You stopped the loop manually. Final x = {x}{RESET}")