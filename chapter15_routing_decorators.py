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

# --- Save user exercises to webapp/routes.py ---

def save_exercises_to_webapp():
    exercises_code = "\n# --- Chapter 15 User Exercises ---\n"

    # Exercise 1: /users/<user_id>/posts/<post_id>
    exercises_code += (
        "import re\n"
        "def user_post_detail(user_id, post_id):\n"
        "    return f'User {user_id}, Post {post_id}'\n"
        "routes[r'^/users/(?P<user_id>\\\\d+)/posts/(?P<post_id>\\\\d+)$'] = user_post_detail\n\n"
    )

    # Exercise 2: decorator with methods
    exercises_code += (
        "def route_with_methods(path_pattern, methods=['GET']):\n"
        "    def decorator(func):\n"
        "        if not hasattr(func, 'methods'):\n"
        "            func.methods = set()\n"
        "        func.methods.update(methods)\n"
        "        routes[path_pattern] = func\n"
        "        return func\n"
        "    return decorator\n\n"
        "@route_with_methods(r'^/ping$', methods=['GET', 'POST'])\n"
        "def ping():\n"
        "    return 'pong'\n\n"
    )

    # Exercise 3: query param support
    exercises_code += (
        "def handle_request_with_query(path, query=None):\n"
        "    for pattern, handler in routes.items():\n"
        "        if (match := re.match(pattern, path)):\n"
        "            if query:\n"
        "                return handler(**match.groupdict(), **query)\n"
        "            else:\n"
        "                return handler(**match.groupdict())\n"
        "    return '404 Not Found'\n\n"
    )

    # Append or update the exercises in webapp/routes.py
    with open('webapp/routes.py', 'r') as f:
        content = f.read()

    marker = '# --- Chapter 15 User Exercises ---'
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

    print("Saved your Chapter 15 exercises to webapp/routes.py!")

if __name__ == "__main__":
    save_exercises_to_webapp()
