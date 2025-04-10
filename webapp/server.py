# webapp/server.py

import asyncio
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

from webapp.routes import routes, get_route
from webapp.models import init_db
from tortoise import run_async

def start_sync_server(host="0.0.0.0", port=8000):
    """
    Start a simple synchronous HTTP server using built-in modules.
    """
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            if (response := get_route(self.path)) is not None:
                self.send_response(200 if response != '404 Not Found' else 404)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(response.encode())
            else:
                self.send_response(404)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(b"404 Not Found")

    server = HTTPServer((host, port), RequestHandler)
    print(f"Starting sync server on http://{host}:{port}")
    server.serve_forever()

async def start_async_server():
    """
    Placeholder for an async server using ASGI (e.g., uvicorn).
    """
    print("Async server placeholder. Run with: uvicorn webapp.server:app --reload")

def start_server():
    """
    Start the web server (sync version in a thread) and initialize the async DB.
    """
    # Initialize async DB in background
    def init_db_task():
        asyncio.run(init_db())

    Thread(target=init_db_task, daemon=True).start()

    # Start sync HTTP server
    start_sync_server()

# Optional: ASGI app for uvicorn/hypercorn
async def app(scope, receive, send):
    """
    Minimal ASGI app compatible with uvicorn/hypercorn.
    """
    assert scope["type"] == "http"
    path = scope["path"]

    if (response_text := get_route(path)) is not None:
        status_code = 200 if response_text != '404 Not Found' else 404
    else:
        response_text = '404 Not Found'
        status_code = 404

    headers = [(b"content-type", b"text/plain")]

    await send({
        "type": "http.response.start",
        "status": status_code,
        "headers": headers
    })
    await send({
        "type": "http.response.body",
        "body": response_text.encode()
    })

if __name__ == "__main__":
    walrus_art = r"""
         __         __
        /  \.-\"\"\"-./  \
        \    -   -    /
         |   o   o   |
         \  .-'''-.  /
          '-\__Y__/-'
             `---`
    """
    print(walrus_art)
    print("Welcome to the Walrus Operator Web Framework!")
    start_server()
