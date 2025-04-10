# Chapter 8: Error Handling

# This chapter introduces try/except, raising exceptions, and handling errors gracefully.

# --- Basic try/except ---

try:
    x = int(input("Enter a number: "))
    print("100 divided by your number is", 100 / x)
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This always runs.")

# --- Raising exceptions ---

def divide(a, b):
    if b == 0:
        raise ValueError("b cannot be zero")
    return a / b

try:
    print(divide(10, 0))
except ValueError as e:
    print("Error:", e)

# --- Mini Web Framework: Error Handling ---

routes = {
    "/": "home page",
    "/about": "about page"
}

def handle_request(url):
    try:
        response = routes[url]
        return f"200 OK: {response}"
    except KeyError:
        return "404 Not Found"

print(handle_request("/"))
print(handle_request("/missing"))

# --- Exercises ---

# Exercise 1:
# Write a program that asks the user for two numbers and divides them, handling invalid input and division by zero.

# Exercise 2:
# Modify the mini web framework to handle unexpected errors gracefully.

# Exercise 3:
# Write a function that raises an exception if a password is too short.
