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
