# Chapter 4: Functional Programming

# This chapter introduces functional programming concepts in Python:
# lambdas, map, filter, reduce, and the Walrus operator (:=)

from functools import reduce
import math

# --- Lambda functions ---

square = lambda x: x * x
print("Square of 5:", square(5))

# --- Map ---

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print("Squared numbers:", squared_numbers)

# --- Filter ---

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# --- Reduce ---

sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", sum_of_numbers)

# --- math.prod() (Python 3.8+) ---

product_of_numbers = math.prod(numbers)
print("Product of numbers:", product_of_numbers)

# --- Walrus operator (Python 3.8+) ---

# Assign and test in one expression
if (n := len(numbers)) > 3:
    print(f"List has {n} elements, which is more than 3")

# --- Mini Web Framework: Functional Routing ---

routes = {
    "/": lambda: "home page",
    "/about": lambda: "about page",
    "/contact": lambda: "contact page"
}

def handle_request(url):
    """Call the route handler function if it exists."""
    if (handler := routes.get(url)) is not None:
        return f"200 OK: {handler()}"
    else:
        return "404 Not Found"

print(handle_request("/"))
print(handle_request("/about"))
print(handle_request("/missing"))

# --- Exercises ---

# Exercise 1:
# Use map() and a lambda to convert a list of temperatures in Celsius to Fahrenheit.

# Exercise 2:
# Use filter() and a lambda to get all words longer than 5 letters from a list of words.

# Exercise 3:
# Use reduce() to multiply all numbers in a list.

# Next chapter: Multithreading!
