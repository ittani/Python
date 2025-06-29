import time
import sys
import random

# ANSI escape codes for color
colors = [
    "\033[91m",  # Red
    "\033[93m",  # Yellow
    "\033[92m",  # Green
    "\033[96m",  # Cyan
    "\033[95m",  # Magenta
    "\033[94m"   # Blue
]
RESET = "\033[0m"

# Spinner frames and fun emojis
spinner = ["🌀", "🌪️", "💫", "✨"]
emojis = ["🚀", "🎯", "🔥", "🤖", "🎮", "🧠", "💡"]

# Random motivational messages
messages = [
    "You're crushing it! 💪",
    "Keep going, genius! 🧠",
    "This loop is 🔥 fire!",
    "Almost there... or are we? 👀",
    "Math is magic! ✨",
    "Don't press Ctrl+C... or do? 🤷‍♂️",
    "x is multiplying like rabbits 🐇"
]

x = 2
frame_index = 0

print(f"\n{random.choice(colors)}🎉 Welcome to the Funky Python Loop Show! Press Ctrl+C to stop. 🎉{RESET}\n")

try:
    while True:
        color = random.choice(colors)
        emoji = random.choice(emojis)
        spinner_frame = spinner[frame_index % len(spinner)]
        message = random.choice(messages)

        sys.stdout.write(
            f"\r{color}{spinner_frame} {emoji} Funky Looping... x = {x} — {message}{RESET}   "
        )
        sys.stdout.flush()
        time.sleep(0.7)

        x *= 2
        frame_index += 1

        if x >= 10000:
            print(f"\n\n\033[1;91m🔔 BOOM! x has reached {x}! Exiting the loop with style! 💥\033[0m\a")
            break

except KeyboardInterrupt:
    print(f"\n\n\033[93m🛑 Funk interrupted! You pressed Ctrl+C. Final x = {x}. Stay groovy! 😎\033[0m")