# Chapter 10: Building a Real Web Server

# This chapter introduces building a simple HTTP server using Python's built-in modules.

from http.server import BaseHTTPRequestHandler, HTTPServer

routes = {
    "/": "home page",
    "/about": "about page"
}

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if (response := routes.get(self.path)) is not None:
            self.send_response(200)
        else:
            response = "404 Not Found"
            self.send_response(404)
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

# --- Save user exercises to webapp/routes.py ---

def save_exercises_to_webapp():
    exercises_code = "\n# --- Chapter 10 User Exercises ---\n"

    # Exercise 1: add more routes (simulate output)
    exercises_code += (
        "def exercise10_1():\n"
        "    return 'Added more routes to the server.'\n\n"
    )

    # Exercise 2: return HTML content (simulate output)
    exercises_code += (
        "def exercise10_2():\n"
        "    return 'Server returns HTML content.'\n\n"
    )

    # Exercise 3: add logging (simulate output)
    exercises_code += (
        "def exercise10_3():\n"
        "    return 'Server logs incoming requests.'\n\n"
    )

    # Append or update the exercises in webapp/routes.py
    with open("webapp/routes.py", "r") as f:
        content = f.read()

    marker = "# --- Chapter 10 User Exercises ---"
    if marker in content:
        pre = content.split(marker)[0]
        post = content.split(marker)[-1]
        post_lines = post.splitlines()
        idx = 0
        for i, line in enumerate(post_lines):
            if line.strip().startswith("# ---"):
                idx = i
                break
        else:
            idx = len(post_lines)
        post = "\n".join(post_lines[idx:])
        new_content = pre + exercises_code + post
    else:
        new_content = content + "\n" + exercises_code

    with open("webapp/routes.py", "w") as f:
        f.write(new_content)

    print("Saved your Chapter 10 exercises to webapp/routes.py!")

if __name__ == "__main__":
    save_exercises_to_webapp()
