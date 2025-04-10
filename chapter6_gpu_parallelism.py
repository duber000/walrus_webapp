# Chapter 6: GPU Parallelism

# This chapter introduces GPU acceleration in Python using Numba and CUDA.
# We'll write simple GPU-accelerated functions and integrate them into our mini web framework.

from numba import cuda
import numpy as np
import math

# --- Basic GPU Kernel ---

@cuda.jit
def add_arrays_kernel(a, b, result):
    idx = cuda.grid(1)
    if idx < a.size:
        result[idx] = a[idx] + b[idx]

# Prepare data
N = 32
a = np.arange(N, dtype=np.float32)
b = np.arange(N, dtype=np.float32)
result = np.zeros(N, dtype=np.float32)

threads_per_block = 8
blocks_per_grid = math.ceil(N / threads_per_block)

# Launch kernel
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
    """Simulate a GPU-accelerated computation as a web response."""
    N = 16
    a = np.arange(N, dtype=np.float32)
    b = np.arange(N, dtype=np.float32)
    result = np.zeros(N, dtype=np.float32)

    threads_per_block = 8
    blocks_per_grid = math.ceil(N / threads_per_block)

    add_arrays_kernel[blocks_per_grid, threads_per_block](a, b, result)

    return f"GPU sum result: {result.tolist()}"

def handle_request(url):
    """Call the route handler function if it exists."""
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
