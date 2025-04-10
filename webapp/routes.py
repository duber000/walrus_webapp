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

# --- Chapter 18: PyTorch Integration ---

import json
from webapp.torch_model import predict_async

async def predict_route_async(scope, receive, send):
    """
    ASGI-compatible async route handler for PyTorch inference.

    Expects POST request with JSON body: {"x": float}

    Responds with JSON: {"input": x, "output": y}
    """
    assert scope["type"] == "http"

    # Wait for request body
    body = b""
    while (message := await receive()).get("more_body", False):
        body += message.get("body", b"")
    body += message.get("body", b"")

    try:
        data = json.loads(body.decode())
        x_value = float(data.get("x", 3.0))
    except Exception:
        x_value = 3.0

    y_value = await predict_async(x_value)

    response_data = {
        "input": x_value,
        "output": y_value
    }
    response_body = json.dumps(response_data).encode()

    headers = [(b"content-type", b"application/json")]

    await send({
        "type": "http.response.start",
        "status": 200,
        "headers": headers
    })
    await send({
        "type": "http.response.body",
        "body": response_body
    })

# Register the async route under a special key
routes['/predict'] = predict_route_async

def get_route(url):
    """
    Synchronous route resolver for simple routes.

    Returns:
        str or callable: response string or async ASGI app.
    """
    handler = routes.get(url)
    return handler if handler is not None else '404 Not Found'


# --- Chapter 2 User Exercises ---
def exercise2_1():
    return 'Positive'

def exercise2_2():
    return 'Even numbers: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20'

def exercise2_3():
    return 'Sum: 0'


from chapter20_external_api import external_users_route_async

routes['/external-users'] = external_users_route_async


# --- Chapter 21: API Client Integration ---

import json as _json
import asyncio as _asyncio

from chapter21_api_client import fetch_users_sync, create_post_sync, fetch_users_async, create_post_async

def external_users_sync():
    """
    Synchronous route that fetches users from an external API.
    """
    users = fetch_users_sync()
    return _json.dumps(users)

routes['/external-users-sync'] = external_users_sync

async def external_users_async_route(scope, receive, send):
    """
    ASGI async route that fetches users from an external API asynchronously.
    """
    users = await fetch_users_async()
    body = _json.dumps(users).encode()

    headers = [(b"content-type", b"application/json")]

    await send({
        "type": "http.response.start",
        "status": 200,
        "headers": headers
    })
    await send({
        "type": "http.response.body",
        "body": body
    })

routes['/external-users-async'] = external_users_async_route

async def create_post_async_route(scope, receive, send):
    """
    ASGI async route that accepts POST JSON input and creates a post via external API.
    """
    assert scope["type"] == "http"

    # Read request body
    body_bytes = b""
    while (message := await receive()).get("more_body", False):
        body_bytes += message.get("body", b"")
    body_bytes += message.get("body", b"")

    try:
        data = _json.loads(body_bytes.decode())
        title = data.get("title", "Untitled")
        body = data.get("body", "")
        user_id = int(data.get("userId", 1))
    except Exception:
        title = "Untitled"
        body = ""
        user_id = 1

    post = await create_post_async(title, body, user_id)
    response_body = _json.dumps(post).encode()

    headers = [(b"content-type", b"application/json")]

    await send({
        "type": "http.response.start",
        "status": 201,
        "headers": headers
    })
    await send({
        "type": "http.response.body",
        "body": response_body
    })

routes['/create-post-async'] = create_post_async_route

