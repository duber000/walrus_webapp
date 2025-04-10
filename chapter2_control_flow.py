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

# --- Pattern Matching (Python 3.10+) ---

command = "start"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case _:
        print("Unknown command")

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

# --- Mini Web Framework: Routing Logic ---

# Let's simulate a simple request URL
request_url = "/about"

# Check if the URL exists in our routes dictionary (defined in Chapter 1)
routes = {
    "/": "home page",
    "/about": "about page"
}

if (response := routes.get(request_url)) is not None:
    print(f"200 OK: {response}")
else:
    print("404 Not Found")

# In the next chapters, we'll turn this into real functions and add more features!

# --- Save user exercises to webapp/routes.py ---

def save_exercises_to_webapp():
    exercises_code = "\n# --- Chapter 2 User Exercises ---\n"

    # Exercise 1: positive, negative, or zero
    num = int(input("Exercise 1 - Enter a number: "))
    if num > 0:
        result1 = "Positive"
    elif num < 0:
        result1 = "Negative"
    else:
        result1 = "Zero"
    exercises_code += f"def exercise2_1():\n    return '{result1}'\n\n"

    # Exercise 2: even numbers from 1 to 20
    evens = [str(i) for i in range(1, 21) if i % 2 == 0]
    exercises_code += f"def exercise2_2():\n    return 'Even numbers: {', '.join(evens)}'\n\n"

    # Exercise 3: sum of numbers until 0
    total = 0
    while True:
        n = int(input("Exercise 3 - Enter a number (0 to stop): "))
        if n == 0:
            break
        total += n
    exercises_code += f"def exercise2_3():\n    return 'Sum: {total}'\n\n"

    # Append or update the exercises in webapp/routes.py
    with open("webapp/routes.py", "r") as f:
        content = f.read()

    marker = "# --- Chapter 2 User Exercises ---"
    if marker in content:
        # Replace existing block
        pre = content.split(marker)[0]
        post = content.split(marker)[-1]
        # Remove everything after marker up to next comment or EOF
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
        # Append at the end
        new_content = content + "\n" + exercises_code

    with open("webapp/routes.py", "w") as f:
        f.write(new_content)

    print("Saved your Chapter 2 exercises to webapp/routes.py!")

if __name__ == "__main__":
    save_exercises_to_webapp()
