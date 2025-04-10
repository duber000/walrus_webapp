# Chapter 6: GPU Parallelism

# This chapter introduces GPU acceleration in Python using Numba and CUDA.
# We'll write simple GPU-accelerated functions and integrate them into our mini web framework.

from numba import cuda
import numpy as np
import math

# --- Basic GPU Kernel ---

# This is a CUDA kernel function that runs on the GPU.
# It adds two arrays element-wise in parallel.
@cuda.jit
def add_arrays_kernel(a, b, result):
    idx = cuda.grid(1)  # Get the absolute thread index within the grid
    if idx < a.size:
        result[idx] = a[idx] + b[idx]

# Prepare data on the host (CPU)
N = 32
a = np.arange(N, dtype=np.float32)
b = np.arange(N, dtype=np.float32)
result = np.zeros(N, dtype=np.float32)

# Define the number of threads per block and blocks per grid
threads_per_block = 8
blocks_per_grid = math.ceil(N / threads_per_block)

# Launch the kernel on the GPU
add_arrays_kernel[blocks_per_grid, threads_per_block](a, b, result)

print("Array A:", a)
print("Array B:", b)
print("Sum (GPU):", result)

# --- Mini Web Framework: GPU-accelerated route ---

routes = {
    "/": lambda: "home page",
    "/about": lambda: "about page",
    "/contact": lambda: "contact page",
    "/gpu-sum": lambda: gpu_sum_route()
}

def gpu_sum_route():
    """
    Simulate a GPU-accelerated computation as a web response.

    This function prepares two arrays, runs the GPU kernel to add them,
    and returns the result as a string.
    """
    N = 16
    a = np.arange(N, dtype=np.float32)
    b = np.arange(N, dtype=np.float32)
    result = np.zeros(N, dtype=np.float32)

    threads_per_block = 8
    blocks_per_grid = math.ceil(N / threads_per_block)

    add_arrays_kernel[blocks_per_grid, threads_per_block](a, b, result)

    return f"GPU sum result: {result.tolist()}"

def handle_request(url):
    """
    Call the route handler function if it exists.

    Args:
        url (str): The request URL.

    Returns:
        str: The HTTP response string.
    """
    if (handler := routes.get(url)) is not None:
        return f"200 OK: {handler()}"
    else:
        return "404 Not Found"

print(handle_request("/"))
print(handle_request("/gpu-sum"))
print(handle_request("/missing"))

# --- Exercises ---

# Exercise 1:
# Write a GPU kernel that multiplies two arrays element-wise.

# Exercise 2:
# Modify the mini web framework to add a new route that uses your GPU multiplication kernel.

# Exercise 3:
# Benchmark the GPU sum against a CPU sum using NumPy and compare the results.

# Congratulations! You've reached the final chapter of this course.
# You now have a basic web framework that uses variables, control flow, functions, functional programming,
# multithreading, and GPU acceleration!

# --- Save user exercises to webapp/routes.py ---

def save_exercises_to_webapp():
    exercises_code = "\n# --- Chapter 6 User Exercises ---\n"

    # Exercise 1: GPU multiply kernel (simulate output)
    exercises_code += (
        "def exercise6_1():\n"
        "    return 'GPU multiplied arrays'\n\n"
    )

    # Exercise 2: new GPU route (simulate output)
    exercises_code += (
        "def exercise6_2():\n"
        "    return 'GPU multiplication route added'\n\n"
    )

    # Exercise 3: benchmark results (simulate output)
    exercises_code += (
        "def exercise6_3():\n"
        "    return 'GPU sum faster than CPU sum'\n\n"
    )

    # Append or update the exercises in webapp/routes.py
    with open("webapp/routes.py", "r") as f:
        content = f.read()

    marker = "# --- Chapter 6 User Exercises ---"
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

    print("Saved your Chapter 6 exercises to webapp/routes.py!")

if __name__ == "__main__":
    save_exercises_to_webapp()
