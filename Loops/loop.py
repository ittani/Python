# learning loops in python
# for loop

# This code will print numbers from 0 to 9
# The range function generates a sequence of numbers
# The for loop iterates over each number in that sequence
# The print function outputs each number to the console

# for i in range(10):
#     print(i)

Vaccines = ["Pfizer", "Moderna", "AstraZeneca", "Johnson & Johnson"]
# This code will print each vaccine name in the list
# The for loop iterates over each item in the Vaccines list
print("\nList of Vaccines available:")
for i in Vaccines:
    print(i)

print("\nFor the rest of the code.")

# While loop
x = 0
while x <= 10:
    print("x is :",x)
    x += 1
    if x == 5:
        print("x is equal to 5, breaking the loop.")
        break

print("\nWhile loop completed.")

# Nested loops
print("\nNested loops example:")
# This code will print pairs of i and j values
# The outer loop iterates over i from 0 to 2
# The inner loop iterates over j from 0 to 1
# The print function outputs the current values of i and j
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")


# printing vaccines vertically
print("\nVaccines printed vertically:")
for vaccine in Vaccines:
    print("") 
    print("I would like to take a short of:")
    for i in vaccine:
        print(i)