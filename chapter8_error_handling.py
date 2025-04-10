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
        if (response := routes.get(url)) is not None:
            return f"200 OK: {response}"
        else:
            return "404 Not Found"
    except Exception:
        return "500 Internal Server Error"

print(handle_request("/"))
print(handle_request("/missing"))

# --- Error Handling with Tortoise ORM queries (sync style) ---

print("\n--- Simulated DB query with error handling ---")

try:
    # This is just a placeholder; real query will be async later
    username = "bob"
    # Imagine: user = await User.get(username=username)
    user = None  # Simulate not found
    if user is None:
        raise LookupError("User not found")
    print("User found:", user)
except LookupError as e:
    print("Error:", e)

# We'll do real async DB queries in the async chapter!

# --- Exercises ---

# Exercise 1:
# Write a program that asks the user for two numbers and divides them, handling invalid input and division by zero.

# Exercise 2:
# Modify the mini web framework to handle unexpected errors gracefully.

# Exercise 3:
# Write a function that raises an exception if a password is too short.

# --- Save user exercises to webapp/routes.py ---

def save_exercises_to_webapp():
    exercises_code = "\n# --- Chapter 8 User Exercises ---\n"

    # Exercise 1: division with error handling (simulate output)
    exercises_code += (
        "def exercise8_1():\n"
        "    return 'Handled division with error handling.'\n\n"
    )

    # Exercise 2: graceful error handling in web framework (simulate output)
    exercises_code += (
        "def exercise8_2():\n"
        "    return 'Web framework handles unexpected errors gracefully.'\n\n"
    )

    # Exercise 3: password validation (simulate output)
    exercises_code += (
        "def exercise8_3():\n"
        "    return 'Password validation with exception works.'\n\n"
    )

    # Append or update the exercises in webapp/routes.py
    with open("webapp/routes.py", "r") as f:
        content = f.read()

    marker = "# --- Chapter 8 User Exercises ---"
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

    print("Saved your Chapter 8 exercises to webapp/routes.py!")

if __name__ == "__main__":
    save_exercises_to_webapp()
