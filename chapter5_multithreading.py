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
