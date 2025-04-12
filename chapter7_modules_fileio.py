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

# --- Introducing Models with Tortoise ORM ---

print("\n--- Defining a User model with Tortoise ORM ---")

from tortoise import fields, models

class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    email = fields.CharField(max_length=100, unique=True)
    is_active = fields.BooleanField(default=True)

    def __str__(self):
        return self.username

print("Defined User model class (no database connection yet).")

# We'll connect to the database and use async queries in a later chapter!

# --- Exercises: Build the Webapp with Modules and File I/O ---

# Exercise 1:
# Add a route /favorite-movies that saves a list of favorite movies to a file and returns a confirmation.

# Exercise 2:
# Add a route /list-movies that reads the movies file and returns a numbered list.

# Exercise 3:
# Add a route /framework-structure that returns a message about splitting the framework into modules.

# --- Save user exercises to webapp/routes.py ---

def save_exercises_to_webapp():
    exercises_code = "\n# --- Chapter 7 User Exercises ---\n"

    # Exercise 1: /favorite-movies
    exercises_code += (
        "def favorite_movies_route():\n"
        "    movies = ['The Matrix', 'Inception', 'Interstellar']\n"
        "    with open('favorite_movies.txt', 'w') as f:\n"
        "        for movie in movies:\n"
        "            f.write(movie + '\\n')\n"
        "    return 'Saved favorite movies to favorite_movies.txt.'\n\n"
        "routes['/favorite-movies'] = favorite_movies_route\n\n"
    )

    # Exercise 2: /list-movies
    exercises_code += (
        "def list_movies_route():\n"
        "    try:\n"
        "        with open('favorite_movies.txt', 'r') as f:\n"
        "            movies = [line.strip() for line in f if line.strip()]\n"
        "        return '\\n'.join([f'{i+1}. {movie}' for i, movie in enumerate(movies)])\n"
        "    except FileNotFoundError:\n"
        "        return 'No favorite_movies.txt file found.'\n\n"
        "routes['/list-movies'] = list_movies_route\n\n"
    )

    # Exercise 3: /framework-structure
    exercises_code += (
        "def framework_structure_route():\n"
        "    return 'Framework split into routes and server modules.'\n\n"
        "routes['/framework-structure'] = framework_structure_route\n\n"
    )

    # Append or update the exercises in webapp/routes.py
    with open('webapp/routes.py', 'r') as f:
        content = f.read()

    marker = '# --- Chapter 7 User Exercises ---'
    if marker in content:
        pre = content.split(marker)[0]
        post = content.split(marker)[-1]
        post_lines = post.splitlines()
        idx = 0
        for i, line in enumerate(post_lines):
            if line.strip().startswith('# ---'):
                idx = i
                break
        else:
            idx = len(post_lines)
        post = '\n'.join(post_lines[idx:])
        new_content = pre + exercises_code + post
    else:
        new_content = content + '\n' + exercises_code

    with open('webapp/routes.py', 'w') as f:
        f.write(new_content)

    print("Saved your Chapter 7 exercises to webapp/routes.py!")

if __name__ == "__main__":
    save_exercises_to_webapp()
