# Chapter 10: Building a Real Web Server

# This chapter introduces building a simple HTTP server using Python's built-in modules.

from http.server import BaseHTTPRequestHandler, HTTPServer

routes = {
    "/": "home page",
    "/about": "about page"
}

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        response = routes.get(self.path, "404 Not Found")
        if response == "404 Not Found":
            self.send_response(404)
        else:
            self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(response.encode())

def run(server_class=HTTPServer, handler_class=SimpleHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()

# --- Exercises ---

# Exercise 1:
# Add more routes and test them in your browser.

# Exercise 2:
# Modify the server to return HTML content.

# Exercise 3:
# Add logging to print each incoming request.
