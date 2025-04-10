# Chapter 3: Functions

# This chapter introduces defining and using functions in Python.

# --- Function Basics ---

def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

print(greet("Alice"))
print(greet("Bob"))

# Function with multiple parameters
def add(a, b):
    """Return the sum of two numbers."""
    return a + b

print("Sum:", add(3, 5))

# Function with default parameter
def power(base, exponent=2):
    """Return base raised to the power of exponent (default is 2)."""
    return base ** exponent

print("Power:", power(3))
print("Power:", power(2, 3))

# --- Mini Web Framework: Refactor routing into a function ---

routes = {
    "/": "home page",
    "/about": "about page",
    "/contact": "contact page"
}

def handle_request(url):
    """Simulate handling a web request by URL."""
    if url in routes:
        return f"200 OK: {routes[url]}"
    else:
        return "404 Not Found"

# Test the routing function
print(handle_request("/"))
print(handle_request("/about"))
print(handle_request("/missing"))

# --- Nested functions ---

def outer():
    print("Inside outer function")

    def inner():
        print("Inside inner function")

    inner()

outer()

# --- Exercises ---

# Exercise 1:
# Write a function `is_even(n)` that returns True if n is even, False otherwise.

# Exercise 2:
# Write a function `factorial(n)` that returns the factorial of n.

# Exercise 3:
# Write a function `greet_user()` that asks the user for their name and prints a greeting.

# In the next chapter, we'll explore functional programming concepts like lambdas, map, filter, reduce, and the Walrus operator!
