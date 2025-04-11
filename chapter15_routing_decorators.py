# Chapter 15: Routing with Path Parameters & Decorators

# This chapter covers dynamic routing, path parameters, and route decorators.

# --- What is a decorator? ---
#
# A decorator is a function that takes another function and returns a new function,
# usually adding some extra behavior. Decorators are a way to "wrap" functions
# to modify or enhance them without changing their code.
#
# In web frameworks, decorators are often used to register route handler functions,
# add authentication, logging, caching, or other cross-cutting concerns.
#
# The @decorator syntax is just a shortcut for:
#
# @my_decorator
# def my_func():
#     pass
#
# which is equivalent to:
#
# def my_func():
#     pass
# my_func = my_decorator(my_func)
#
# In this chapter, we use decorators to register URL patterns with handler functions.

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
