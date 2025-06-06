# Chapter 5: Multithreading

# This chapter introduces multithreading in Python using the threading module.

import threading
import time

# --- Basic Thread Example ---

def print_numbers():
    for i in range(5):
        print(f"[Thread] Number: {i}")
        time.sleep(0.5)

# Create a thread
thread = threading.Thread(target=print_numbers)

# Start the thread
thread.start()

# Main thread continues
for i in range(5):
    print(f"[Main] Letter: {chr(65 + i)}")
    time.sleep(0.5)

# Wait for the thread to finish
thread.join()

print("Both threads finished.")

# --- Mini Web Framework: Multithreaded Request Handling ---

routes = {
    "/": lambda: "home page",
    "/about": lambda: "about page",
    "/contact": lambda: "contact page"
}

def handle_request(url):
    """Simulate handling a web request."""
    if (handler := routes.get(url)) is not None:
        response = handler()
        print(f"200 OK: {response}")
    else:
        print("404 Not Found")

def serve_request(url):
    """Thread target for serving a request."""
    print(f"Handling request for {url}")
    handle_request(url)

# Simulate multiple incoming requests
urls = ["/", "/about", "/missing", "/contact"]

threads = []
for url in urls:
    t = threading.Thread(target=serve_request, args=(url,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("All requests handled.")

# --- Exercises: Build the Webapp with Multithreading ---

# Exercise 1:
# Add a route /thread-count that starts a thread to count from 1 to 5 and returns the result.

# Exercise 2:
# Add a route /thread-messages that starts two threads, each printing a different message, and returns their output.

# Exercise 3:
# Add a route /concurrent-requests that simulates handling 10 requests concurrently and returns a summary.

# Next chapter: GPU parallelism!

# --- Save user exercises to webapp/routes.py ---

def save_exercises_to_webapp():
    import threading
    import time

    exercises_code = "\n# --- Chapter 5 User Exercises ---\n"

    # Exercise 1: /thread-count
    exercises_code += (
        "def thread_count_route():\n"
        "    result = []\n"
        "    def count():\n"
        "        for i in range(1, 6):\n"
        "            result.append(str(i))\n"
        "            time.sleep(0.05)\n"
        "    t = threading.Thread(target=count)\n"
        "    t.start()\n"
        "    t.join()\n"
        "    return 'Threaded count: ' + ' '.join(result)\n\n"
        "routes['/thread-count'] = thread_count_route\n\n"
    )

    # Exercise 2: /thread-messages
    exercises_code += (
        "def thread_messages_route():\n"
        "    output = []\n"
        "    def a():\n"
        "        output.append('Thread A: Hello')\n"
        "    def b():\n"
        "        output.append('Thread B: World')\n"
        "    t1 = threading.Thread(target=a)\n"
        "    t2 = threading.Thread(target=b)\n"
        "    t1.start()\n"
        "    t2.start()\n"
        "    t1.join()\n"
        "    t2.join()\n"
        "    return ' | '.join(output)\n\n"
        "routes['/thread-messages'] = thread_messages_route\n\n"
    )

    # Exercise 3: /concurrent-requests
    exercises_code += (
        "def concurrent_requests_route():\n"
        "    results = []\n"
        "    def handle(i):\n"
        "        results.append(f'Request {i} handled')\n"
        "    threads = []\n"
        "    for i in range(10):\n"
        "        t = threading.Thread(target=handle, args=(i+1,))\n"
        "        t.start()\n"
        "        threads.append(t)\n"
        "    for t in threads:\n"
        "        t.join()\n"
        "    return ' | '.join(results)\n\n"
        "routes['/concurrent-requests'] = concurrent_requests_route\n\n"
    )

    # Append or update the exercises in webapp/routes.py
    with open("webapp/routes.py", "r") as f:
        content = f.read()

    marker = "# --- Chapter 5 User Exercises ---"
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

    print("Saved your Chapter 5 exercises to webapp/routes.py!")

if __name__ == "__main__":
    save_exercises_to_webapp()
