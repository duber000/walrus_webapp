# Chapter 13: HTTP Protocol, REST APIs, and JSON

# This chapter explains HTTP methods, status codes, REST API design, and JSON handling.

import json

# --- HTTP Methods ---

# GET: retrieve data
# POST: create new resource
# PUT: update existing resource
# DELETE: remove resource
# PATCH: partial update

# --- Status Codes ---

# 200 OK, 201 Created, 204 No Content
# 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found
# 500 Internal Server Error

# --- REST API Design Principles ---

# - Use nouns for resources: /users, /posts
# - Use HTTP methods to define actions
# - Use plural resource names
# - Use status codes appropriately
# - Support filtering, sorting, pagination via query params

# --- JSON Serialization ---

# JSON serialization is the process of converting Python objects (like dicts, lists)
# into a JSON-formatted string, which can be sent over the network or saved to a file.
# JSON (JavaScript Object Notation) is a lightweight, text-based data format widely used
# for data exchange between clients and servers.
# The reverse process, turning a JSON string back into Python objects, is called deserialization.

user = {
    "id": 1,
    "username": "alice",
    "email": "alice@example.com"
}

json_str = json.dumps(user)
print("Serialized JSON:", json_str)

parsed = json.loads(json_str)
print("Parsed JSON:", parsed)

# --- Mini Web Framework: RESTful routes ---

routes = {
    "/users": lambda: json.dumps([{"id": 1, "username": "alice"}]),
    "/posts": lambda: json.dumps([])
}

def handle_request(path, method="GET", body=None):
    if method == "GET":
        if (handler := routes.get(path)) is not None:
            return 200, handler()
        else:
            return 404, "Not Found"
    elif method == "POST":
        # Simulate creating a resource
        return 201, "Created"
    else:
        return 405, "Method Not Allowed"

status, response = handle_request("/users")
print(f"Status: {status}, Response: {response}")

status, response = handle_request("/unknown")
print(f"Status: {status}, Response: {response}")

# --- Exercises ---

# Exercise 1:
# Add a /products route that returns a JSON list of products.

# Exercise 2:
# Simulate POST request handling to add a new user.

# Exercise 3:
# Parse a JSON request body and extract fields.

# --- Save user exercises to webapp/routes.py ---

def save_exercises_to_webapp():
    exercises_code = "\n# --- Chapter 13 User Exercises ---\n"

    # Exercise 1: /products
    exercises_code += (
        "def products_route():\n"
        "    products = [\n"
        "        {'id': 1, 'name': 'Widget', 'price': 9.99},\n"
        "        {'id': 2, 'name': 'Gadget', 'price': 14.99},\n"
        "        {'id': 3, 'name': 'Thingamajig', 'price': 4.99},\n"
        "    ]\n"
        "    import json\n"
        "    return json.dumps(products)\n\n"
        "routes['/products'] = products_route\n\n"
    )

    # Exercise 2: /add-user (POST)
    exercises_code += (
        "def add_user_route(body=None):\n"
        "    import json\n"
        "    if body is None:\n"
        "        return 'No data provided.'\n"
        "    try:\n"
        "        data = json.loads(body)\n"
        "        username = data.get('username', 'unknown')\n"
        "        return f'User {username} added!'\n"
        "    except Exception:\n"
        "        return 'Invalid JSON.'\n\n"
        "routes['/add-user'] = add_user_route\n\n"
    )

    # Exercise 3: /parse-json
    exercises_code += (
        "def parse_json_route(body=None):\n"
        "    import json\n"
        "    try:\n"
        "        data = json.loads(body)\n"
        "        return f\"Parsed fields: {list(data.keys())}\"\n"
        "    except Exception:\n"
        "        return 'Invalid JSON.'\n\n"
        "routes['/parse-json'] = parse_json_route\n\n"
    )

    # Append or update the exercises in webapp/routes.py
    with open('webapp/routes.py', 'r') as f:
        content = f.read()

    marker = '# --- Chapter 13 User Exercises ---'
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

    print("Saved your Chapter 13 exercises to webapp/routes.py!")

if __name__ == "__main__":
    save_exercises_to_webapp()
