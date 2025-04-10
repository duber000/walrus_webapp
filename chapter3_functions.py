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

# --- Save user exercises to webapp/routes.py ---

def save_exercises_to_webapp():
    exercises_code = "\n# --- Chapter 3 User Exercises ---\n"

    # Exercise 1: is_even
    def is_even(n):
        return n % 2 == 0

    exercises_code += (
        "def exercise3_1(n):\n"
        "    return 'Even' if n % 2 == 0 else 'Odd'\n\n"
    )

    # Exercise 2: factorial
    def factorial(n):
        return 1 if n == 0 else n * factorial(n - 1)

    exercises_code += (
        "def exercise3_2(n):\n"
        "    result = 1\n"
        "    for i in range(1, n + 1):\n"
        "        result *= i\n"
        "    return f'Factorial: {result}'\n\n"
    )

    # Exercise 3: greet_user
    name = input("Exercise 3 - Enter your name: ")
    exercises_code += (
        f"def exercise3_3():\n"
        f"    return 'Hello, {name}!'\n\n"
    )

    # Append or update the exercises in webapp/routes.py
    with open("webapp/routes.py", "r") as f:
        content = f.read()

    marker = "# --- Chapter 3 User Exercises ---"
    if marker in content:
        pre = content.split(marker)[0]
        post = content.split(marker)[-1]
        post_lines = post.splitlines()
        idx = 0
        for i, line in enumerate(post_lines):
            if line.strip().startswith("# ---"):
                idx = i
                break
        else:
            idx = len(post_lines)
        post = "\n".join(post_lines[idx:])
        new_content = pre + exercises_code + post
    else:
        new_content = content + "\n" + exercises_code

    with open("webapp/routes.py", "w") as f:
        f.write(new_content)

    print("Saved your Chapter 3 exercises to webapp/routes.py!")

if __name__ == "__main__":
    save_exercises_to_webapp()
