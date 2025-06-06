# Chapter 4: Functional Programming

# This chapter introduces functional programming concepts in Python:
# lambdas, map, filter, reduce, and the Walrus operator (:=)

from functools import reduce

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

# --- Product of numbers (without math.prod) ---

product_of_numbers = 1
for num in numbers:
    product_of_numbers *= num
print("Product of numbers:", product_of_numbers)

# --- Walrus operator (Python 3.8+) ---

# The walrus operator := allows assignment inside expressions.
# For example, assign and test in one line:
if (n := len(numbers)) > 3:
    print(f"List has {n} elements, which is more than 3")

# Another example: reading input until empty string
# Uncomment to try:
# while (line := input("Enter text (empty to stop): ")) != "":
#     print("You entered:", line)

# --- Mini Web Framework: Functional Routing ---

# Sample user data to demonstrate map, filter, reduce in a realistic web context
users = [
    {"username": "alice", "age": 30, "active": True},
    {"username": "bob", "age": 25, "active": False},
    {"username": "carol", "age": 27, "active": True},
    {"username": "dave", "age": 22, "active": True},
]

routes = {
    "/": lambda: "home page",
    "/about": lambda: "about page",
    "/contact": lambda: "contact page",

    # Map: list all usernames
    "/usernames": lambda: f"Usernames: {list(map(lambda u: u['username'], users))}",

    # Filter: show only active users
    "/active-users": lambda: f"Active users: {list(filter(lambda u: u['active'], users))}",

    # Map + filter: usernames of active users
    "/active-usernames": lambda: f"Active usernames: {list(map(lambda u: u['username'], filter(lambda u: u['active'], users)))}",

    # Reduce: total age of all users
    "/total-age": lambda: f"Total age: {reduce(lambda acc, u: acc + u['age'], users, 0)}",

    # Reduce: count active users
    "/count-active": lambda: f"Active user count: {reduce(lambda acc, u: acc + (1 if u['active'] else 0), users, 0)}",
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
print(handle_request("/usernames"))
print(handle_request("/active-users"))
print(handle_request("/active-usernames"))
print(handle_request("/total-age"))
print(handle_request("/count-active"))

# --- Exercises: Build the Webapp with Functional Programming ---

# Exercise 1:
# Add a route /celsius-to-fahrenheit that returns a list of Celsius temperatures converted to Fahrenheit.

# Exercise 2:
# Add a route /long-words that returns all words longer than 5 letters from a list.

# Exercise 3:
# Add a route /product that returns the product of numbers in a list.

# Next chapter: Multithreading!

# --- Save user exercises to webapp/routes.py ---

def save_exercises_to_webapp():
    exercises_code = "\n# --- Chapter 4 User Exercises ---\n"

    # Exercise 1: /celsius-to-fahrenheit
    exercises_code += (
        "def celsius_to_fahrenheit_route():\n"
        "    celsius_list = [0, 10, 20, 30]\n"
        "    fahrenheit_list = list(map(lambda c: c * 9/5 + 32, celsius_list))\n"
        "    return 'Fahrenheit: ' + str(fahrenheit_list)\n\n"
        "routes['/celsius-to-fahrenheit'] = celsius_to_fahrenheit_route\n\n"
    )

    # Exercise 2: /long-words
    exercises_code += (
        "def long_words_route():\n"
        "    words = ['apple', 'banana', 'cherry', 'date', 'elderberry']\n"
        "    long_words = list(filter(lambda w: len(w) > 5, words))\n"
        "    return 'Long words: ' + str(long_words)\n\n"
        "routes['/long-words'] = long_words_route\n\n"
    )

    # Exercise 3: /product
    exercises_code += (
        "def product_route():\n"
        "    from functools import reduce\n"
        "    nums = [1, 2, 3, 4, 5]\n"
        "    product = reduce(lambda x, y: x * y, nums)\n"
        "    return f'Product: {product}'\n\n"
        "routes['/product'] = product_route\n\n"
    )

    # Append or update the exercises in webapp/routes.py
    with open("webapp/routes.py", "r") as f:
        content = f.read()

    marker = "# --- Chapter 4 User Exercises ---"
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

    print("Saved your Chapter 4 exercises to webapp/routes.py!")

if __name__ == "__main__":
    save_exercises_to_webapp()
