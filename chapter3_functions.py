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
    if (response := routes.get(url)) is not None:
        return f"200 OK: {response}"
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

# --- Exercises: Build the Webapp with Functions ---

# Exercise 1:
# Add a route /is-even/<n> that returns "Even" or "Odd" based on whether n is even.

# Exercise 2:
# Add a route /factorial/<n> that returns the factorial of n.

# Exercise 3:
# Add a route /greet-user/<name> that returns a personalized greeting.

# In the next chapter, we'll explore functional programming concepts like lambdas, map, filter, reduce, and the Walrus operator!

# --- Save user exercises to webapp/routes.py ---

def save_exercises_to_webapp():
    exercises_code = "\n# --- Chapter 3 User Exercises ---\n"

    # Exercise 1: /is-even/<n>
    exercises_code += (
        "def is_even_route(n):\n"
        "    n = int(n)\n"
        "    return 'Even' if n % 2 == 0 else 'Odd'\n\n"
        "routes['/is-even/<n>'] = is_even_route\n\n"
    )

    # Exercise 2: /factorial/<n>
    exercises_code += (
        "def factorial_route(n):\n"
        "    n = int(n)\n"
        "    result = 1\n"
        "    for i in range(1, n + 1):\n"
        "        result *= i\n"
        "    return f'Factorial: {result}'\n\n"
        "routes['/factorial/<n>'] = factorial_route\n\n"
    )

    # Exercise 3: /greet-user/<name>
    exercises_code += (
        "def greet_user_route(name):\n"
        "    return f'Hello, {name}!'\n\n"
        "routes['/greet-user/<name>'] = greet_user_route\n\n"
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
