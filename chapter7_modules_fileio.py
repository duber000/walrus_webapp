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
