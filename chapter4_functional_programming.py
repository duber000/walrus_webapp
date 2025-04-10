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

# --- Save user exercises to webapp/routes.py ---

def save_exercises_to_webapp():
    exercises_code = "\n# --- Chapter 4 User Exercises ---\n"

    # Exercise 1: Celsius to Fahrenheit
    celsius_list = [0, 10, 20, 30]
    fahrenheit_list = list(map(lambda c: c * 9/5 + 32, celsius_list))
    exercises_code += (
        f"def exercise4_1():\n"
        f"    return 'Fahrenheit: {fahrenheit_list}'\n\n"
    )

    # Exercise 2: words longer than 5 letters
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    long_words = list(filter(lambda w: len(w) > 5, words))
    exercises_code += (
        f"def exercise4_2():\n"
        f"    return 'Long words: {long_words}'\n\n"
    )

    # Exercise 3: product of numbers
    from functools import reduce
    nums = [1, 2, 3, 4, 5]
    product = reduce(lambda x, y: x * y, nums)
    exercises_code += (
        f"def exercise4_3():\n"
        f"    return 'Product: {product}'\n\n"
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
