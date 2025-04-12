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
    if (path := request.path) == "/":
        return Response("Home page")
    elif path == "/hello":
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

# --- Save user exercises to webapp/routes.py ---

def save_exercises_to_webapp():
    exercises_code = "\n# --- Chapter 14 User Exercises ---\n"

    # Exercise 1: /custom-header-middleware
    exercises_code += (
        "def custom_header_middleware(request, next_handler):\n"
        "    response = next_handler(request)\n"
        "    response.headers['X-Custom-Header'] = 'MyValue'\n"
        "    return response\n\n"
    )

    # Exercise 2: /parse-query
    exercises_code += (
        "def parse_query_route(request):\n"
        "    # Simulate parsing query params from URL\n"
        "    from urllib.parse import urlparse, parse_qs\n"
        "    parsed = urlparse(request.path)\n"
        "    query = parse_qs(parsed.query)\n"
        "    return f'Query params: {query}'\n\n"
        "routes['/parse-query'] = parse_query_route\n\n"
    )

    # Exercise 3: /chain-middlewares
    exercises_code += (
        "def auth_middleware(request, next_handler):\n"
        "    # Simulate auth check\n"
        "    if getattr(request, 'user', None) == 'admin':\n"
        "        return next_handler(request)\n"
        "    else:\n"
        "        from dataclasses import dataclass\n"
        "        @dataclass\n"
        "        class Response:\n"
        "            content: str\n"
        "            status: int = 403\n"
        "            headers: dict = None\n"
        "        return Response('Forbidden', status=403)\n\n"
        "def chain_middlewares_route(request):\n"
        "    # Simulate chaining logging and auth middleware\n"
        "    def handler(req):\n"
        "        from dataclasses import dataclass\n"
        "        @dataclass\n"
        "        class Response:\n"
        "            content: str\n"
        "            status: int = 200\n"
        "            headers: dict = None\n"
        "        return Response('OK')\n"
        "    # Compose middlewares\n"
        "    def logging_mw(req, next_handler):\n"
        "        print(f'[LOG] {req.method} {req.path}')\n"
        "        return next_handler(req)\n"
        "    composed = lambda req: auth_middleware(req, lambda r: logging_mw(r, handler))\n"
        "    return composed(request)\n\n"
        "routes['/chain-middlewares'] = chain_middlewares_route\n\n"
    )

    # Append or update the exercises in webapp/routes.py
    with open('webapp/routes.py', 'r') as f:
        content = f.read()

    marker = '# --- Chapter 14 User Exercises ---'
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

    print("Saved your Chapter 14 exercises to webapp/routes.py!")

if __name__ == "__main__":
    save_exercises_to_webapp()
