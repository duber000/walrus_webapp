# Chapter 14: Request & Response Abstractions, Middleware

# This chapter introduces request parsing, response objects, and middleware pattern.

import json
from dataclasses import dataclass, field

# --- Request and Response Classes ---

@dataclass
class Request:
    path: str
    method: str = "GET"
    headers: dict = field(default_factory=dict)
    query_params: dict = field(default_factory=dict)
    body: str = ""

@dataclass
class Response:
    content: str
    status: int = 200
    headers: dict = field(default_factory=lambda: {"Content-Type": "text/plain"})

# --- Middleware Pattern ---

def logging_middleware(request: Request, next_handler):
    print(f"[LOG] {request.method} {request.path}")
    response = next_handler(request)
    print(f"[LOG] Response status: {response.status}")
    return response

def simple_handler(request: Request) -> Response:
    if request.path == "/":
        return Response("Home page")
    elif request.path == "/hello":
        return Response("Hello world!")
    else:
        return Response("Not Found", status=404)

def apply_middlewares(handler, middlewares):
    for mw in reversed(middlewares):
        next_handler = handler
        handler = lambda req, mw=mw, next_handler=next_handler: mw(req, next_handler)
    return handler

middlewares = [logging_middleware]
app = apply_middlewares(simple_handler, middlewares)

req = Request(path="/hello")
res = app(req)
print(f"Response: {res.status} {res.content}")

# --- Exercises ---

# Exercise 1:
# Add a middleware that adds a custom header to the response.

# Exercise 2:
# Parse query parameters from a URL string into the Request object.

# Exercise 3:
# Chain multiple middlewares (e.g., logging, auth check).
