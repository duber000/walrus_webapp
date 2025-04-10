# Chapter 1: Variables and Data Types

# This chapter introduces Python variables and basic data types.

# Integer
age = 25
print("Age:", age)

# Float
height = 1.75
print("Height in meters:", height)

# String
name = "Alice"
print("Name:", name)

# Boolean
is_student = True
print("Is a student:", is_student)

# List
colors = ["red", "green", "blue"]
print("Favorite colors:", colors)

# Tuple
coordinates = (10.0, 20.0)
print("Coordinates:", coordinates)

# Dictionary
person = {"name": "Bob", "age": 30}
print("Person info:", person)

# Set
unique_numbers = {1, 2, 3, 2, 1}
print("Unique numbers:", unique_numbers)

# NoneType
nothing = None
print("Nothing:", nothing)

# Exercise 1:
# Create a variable called 'city' and assign your city name to it.
# Then print "I live in <city>"

# Exercise 2:
# Create a list of your three favorite foods and print it.

# Exercise 3:
# Create a dictionary with keys 'first_name' and 'last_name' and your own values, then print it.

# --- Mini Web Framework Start ---

# In this course, we'll build a simple web framework step by step.
# For now, let's just define a dictionary to hold our "routes".

routes = {
    "/": "home page",
    "/about": "about page"
}

print("Available routes:", routes)

# We'll add more functionality in the next chapters!
