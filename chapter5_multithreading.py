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

# --- Exercises ---

# Exercise 1:
# Write a function that prints numbers 1-5 with a delay, and run it in a thread.

# Exercise 2:
# Create two threads that print different messages, and run them simultaneously.

# Exercise 3:
# Modify the mini web framework to simulate handling 10 requests concurrently.

# Next chapter: GPU parallelism!

# --- Save user exercises to webapp/routes.py ---

def save_exercises_to_webapp():
    exercises_code = "\n# --- Chapter 5 User Exercises ---\n"

    # Exercise 1: print numbers 1-5 with delay (simulate output)
    exercises_code += (
        "def exercise5_1():\n"
        "    return 'Threaded count: 1 2 3 4 5'\n\n"
    )

    # Exercise 2: two threads with different messages (simulate output)
    exercises_code += (
        "def exercise5_2():\n"
        "    return 'Thread A: Hello | Thread B: World'\n\n"
    )

    # Exercise 3: simulate 10 concurrent requests
    exercises_code += (
        "def exercise5_3():\n"
        "    return 'Handled 10 concurrent requests'\n\n"
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
