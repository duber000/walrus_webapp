# webapp/routes.py

# Base routes from Chapter 1
routes = {
    '/': 'home page',
    '/about': 'about page'
}

# Chapter 2: Control Flow - add a /age route
def age_category(age):
    if age < 13:
        return "You are a child."
    elif age < 20:
        return "You are a teenager."
    else:
        return "You are an adult."

routes['/age'] = lambda: age_category(20)

# Chapter 3: Functions - add a /greet route
def greet(name="Alice"):
    return f"Hello, {name}!"

routes['/greet'] = lambda: greet()

# Chapter 4: Functional Programming - add a /squares route
def squares():
    nums = [1, 2, 3, 4, 5]
    return f"Squares: {[x * x for x in nums]}"

routes['/squares'] = squares

# Chapter 5: Multithreading - simulate with a /thread-demo route
def thread_demo():
    return "Threading demo placeholder"

routes['/thread-demo'] = thread_demo

# Chapter 6: GPU Parallelism - simulate with a /gpu-demo route
def gpu_demo():
    return "GPU demo placeholder"

routes['/gpu-demo'] = gpu_demo

# Chapter 7: Modules and File I/O - add a /file-content route
def file_content():
    try:
        with open("output.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        return "File not found."

routes['/file-content'] = file_content

# Chapter 8: Error Handling - add a /error-test route
def error_test():
    try:
        return str(100 / 0)
    except ZeroDivisionError:
        return "Cannot divide by zero!"

routes['/error-test'] = error_test

# Chapter 9: OOP - add a /user route
from dataclasses import dataclass

@dataclass
class User:
    username: str
    email: str

def user_info():
    user = User("alice", "alice@example.com")
    return f"User: {user.username}, Email: {user.email}"

routes['/user'] = user_info

# Chapter 10: Web Server - no new route, but this file is used by the server

# Placeholder for future async routes (Chapter 12)
# Example:
# async def async_users_route():
#     users = await User.all()
#     return ", ".join([u.username for u in users])

def get_route(url):
    if (handler := routes.get(url)) is not None:
        if callable(handler):
            return handler()
        else:
            return handler
    else:
        return '404 Not Found'


# --- Chapter 2 User Exercises ---
def exercise2_1():
    return 'Positive'

def exercise2_2():
    return 'Even numbers: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20'

def exercise2_3():
    return 'Sum: 0'

