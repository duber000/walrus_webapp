# Chapter 6: GPU Parallelism

# This chapter introduces GPU acceleration in Python using Numba and CUDA.
# We'll write simple GPU-accelerated functions and integrate them into our mini web framework.

from numba import cuda
import numpy as np

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
blocks_per_grid = (N + threads_per_block - 1) // threads_per_block  # simple integer division

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
    blocks_per_grid = (N + threads_per_block - 1) // threads_per_block  # simple integer division

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

# --- Exercises: Build the Webapp with GPU Parallelism ---

# Exercise 1:
# Add a GPU kernel that multiplies two arrays element-wise.

# Exercise 2:
# Add a /gpu-multiply route that uses your GPU multiplication kernel and returns the result.

# Exercise 3:
# Add a /gpu-vs-cpu-benchmark route that benchmarks GPU sum vs CPU sum and returns the timing.

# Congratulations! You've reached the final chapter of this course.
# You now have a basic web framework that uses variables, control flow, functions, functional programming,
# multithreading, and GPU acceleration!

# --- Save user exercises to webapp/routes.py ---

def save_exercises_to_webapp():
    exercises_code = "\n# --- Chapter 6 User Exercises ---\n"

    # Exercise 1: GPU multiply kernel
    exercises_code += (
        "from numba import cuda\n"
        "import numpy as np\n"
        "\n"
        "@cuda.jit\n"
        "def multiply_arrays_kernel(a, b, result):\n"
        "    idx = cuda.grid(1)\n"
        "    if idx < a.size:\n"
        "        result[idx] = a[idx] * b[idx]\n\n"
    )

    # Exercise 2: /gpu-multiply route
    exercises_code += (
        "def gpu_multiply_route():\n"
        "    N = 16\n"
        "    a = np.arange(N, dtype=np.float32)\n"
        "    b = np.arange(N, dtype=np.float32)\n"
        "    result = np.zeros(N, dtype=np.float32)\n"
        "    threads_per_block = 8\n"
        "    blocks_per_grid = (N + threads_per_block - 1) // threads_per_block\n"
        "    multiply_arrays_kernel[blocks_per_grid, threads_per_block](a, b, result)\n"
        "    return 'GPU multiply result: ' + str(result.tolist())\n\n"
        "routes['/gpu-multiply'] = gpu_multiply_route\n\n"
    )

    # Exercise 3: /gpu-vs-cpu-benchmark route
    exercises_code += (
        "import time\n"
        "def gpu_vs_cpu_benchmark_route():\n"
        "    N = 1000000\n"
        "    a = np.arange(N, dtype=np.float32)\n"
        "    b = np.arange(N, dtype=np.float32)\n"
        "    result_gpu = np.zeros(N, dtype=np.float32)\n"
        "    threads_per_block = 256\n"
        "    blocks_per_grid = (N + threads_per_block - 1) // threads_per_block\n"
        "    start_gpu = time.time()\n"
        "    add_arrays_kernel[blocks_per_grid, threads_per_block](a, b, result_gpu)\n"
        "    gpu_time = time.time() - start_gpu\n"
        "    start_cpu = time.time()\n"
        "    result_cpu = a + b\n"
        "    cpu_time = time.time() - start_cpu\n"
        "    return f'GPU time: {gpu_time:.6f}s, CPU time: {cpu_time:.6f}s'\n\n"
        "routes['/gpu-vs-cpu-benchmark'] = gpu_vs_cpu_benchmark_route\n\n"
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
