# Chapter 7: Modules and File I/O

# This chapter introduces splitting code into modules and reading/writing files.

# --- Modules ---

# Suppose this is in routes.py
routes = {
    "/": "home page",
    "/about": "about page"
}

def handle_request(url):
    if url in routes:
        return f"200 OK: {routes[url]}"
    else:
        return "404 Not Found"

# In another file, you would import like:
# from routes import handle_request

# --- File I/O ---

# Write to a file
with open("output.txt", "w") as f:
    f.write("Hello, file!\n")
    f.write("Another line.\n")

# Read from a file
with open("output.txt", "r") as f:
    content = f.read()
    print("File content:\n", content)

# --- Exercises ---

# Exercise 1:
# Write a program that saves a list of your favorite movies to a file, one per line.

# Exercise 2:
# Write a program that reads the movies file and prints each movie with a number.

# Exercise 3:
# Split your mini web framework into two files: one for routes, one for the server logic.

# --- Save user exercises to webapp/routes.py ---

def save_exercises_to_webapp():
    exercises_code = "\n# --- Chapter 7 User Exercises ---\n"

    # Exercise 1: save favorite movies (simulate output)
    exercises_code += (
        "def exercise7_1():\n"
        "    return 'Saved favorite movies to file.'\n\n"
    )

    # Exercise 2: read movies and print numbered list (simulate output)
    exercises_code += (
        "def exercise7_2():\n"
        "    return '1. Movie A\\n2. Movie B\\n3. Movie C'\n\n"
    )

    # Exercise 3: split framework into modules (simulate output)
    exercises_code += (
        "def exercise7_3():\n"
        "    return 'Split framework into routes and server modules.'\n\n"
    )

    # Append or update the exercises in webapp/routes.py
    with open("webapp/routes.py", "r") as f:
        content = f.read()

    marker = "# --- Chapter 7 User Exercises ---"
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

    print("Saved your Chapter 7 exercises to webapp/routes.py!")

if __name__ == "__main__":
    save_exercises_to_webapp()
