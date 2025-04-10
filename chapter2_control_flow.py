# Chapter 2: Control Flow

# This chapter introduces conditionals and loops in Python.

# --- Conditionals ---

age = 20

if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")

# --- Comparison operators ---
# ==, !=, <, >, <=, >=

number = 7

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# --- Logical operators ---
# and, or, not

is_raining = False
is_cold = True

if is_raining and is_cold:
    print("Wear a raincoat and a sweater.")
elif is_raining and not is_cold:
    print("Wear a raincoat.")
elif not is_raining and is_cold:
    print("Wear a sweater.")
else:
    print("Enjoy the weather!")

# --- Loops ---

# While loop
count = 0
while count < 5:
    print("Counting:", count)
    count += 1

# For loop over a list
colors = ["red", "green", "blue"]
for color in colors:
    print("Color:", color)

# For loop with range
for i in range(1, 6):
    print("Number:", i)

# --- Loop control statements ---
# break, continue

for i in range(10):
    if i == 3:
        continue  # skip 3
    if i == 7:
        break     # stop loop at 7
    print("i =", i)

# --- Exercises ---

# Exercise 1:
# Write a program that asks the user for a number and prints whether it is positive, negative, or zero.

# Exercise 2:
# Write a program that prints all even numbers from 1 to 20 using a for loop.

# Exercise 3:
# Write a program that asks the user to enter numbers repeatedly until they enter 0, then prints the sum of all entered numbers.
