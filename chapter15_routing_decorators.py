# Chapter 15: Routing with Path Parameters & Decorators

# This chapter covers dynamic routing, path parameters, and route decorators.

import re

routes = {}

def route(path_pattern):
    def decorator(func):
        routes[path_pattern] = func
        return func
    return decorator

@route(r"^/users/(?P<user_id>\d+)$")
def user_detail(user_id):
    return f"User detail for user_id={user_id}"

@route(r"^/posts/(?P<slug>[\w-]+)$")
def post_detail(slug):
    return f"Post detail for slug={slug}"

def handle_request(path):
    for pattern, handler in routes.items():
        if (match := re.match(pattern, path)):
            return handler(**match.groupdict())
    return "404 Not Found"

print(handle_request("/users/42"))
print(handle_request("/posts/hello-world"))
print(handle_request("/unknown"))

# --- Exercises ---

# Exercise 1:
# Add a route with multiple path parameters, e.g., /users/<user_id>/posts/<post_id>

# Exercise 2:
# Add a decorator argument to specify allowed HTTP methods.

# Exercise 3:
# Refactor the routing system to support query parameters.
