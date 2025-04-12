# Chapter 11: Testing and Debugging

# This chapter introduces writing tests and debugging Python code.

from dataclasses import dataclass

# We'll use a dataclass as a simple Data Transfer Object (DTO) to hold test results.
# DTOs are plain data containers that make it easy to pass structured data around.
@dataclass
class TestResult:
    name: str
    passed: bool
    message: str = ""

# --- Using assert ---

def add(a, b):
    return a + b

assert add(2, 3) == 5
assert add(-1, 1) == 0

print("All asserts passed.")

# --- Using unittest ---

import unittest

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 2), 4)
        self.assertEqual(add(-1, 1), 0)

def run_simple_tests():
    results = []
    try:
        assert add(2, 2) == 4
        results.append(TestResult("add 2+2", True))
    except AssertionError:
        results.append(TestResult("add 2+2", False, "Expected 4"))

    try:
        assert add(-1, 1) == 0
        results.append(TestResult("add -1+1", True))
    except AssertionError:
        results.append(TestResult("add -1+1", False, "Expected 0"))

    for r in results:
        print(f"Test '{r.name}': {'PASSED' if r.passed else 'FAILED'} {r.message}")

if __name__ == "__main__":
    unittest.main()
    run_simple_tests()

# --- Debugging tips ---

# Use print() statements to trace values.
# Use the built-in breakpoint() function (Python 3.7+):
breakpoint()

# --- Exercises ---

# Exercise 1:
# Write tests for your mini web framework's request handler.

# Exercise 2:
# Intentionally introduce a bug and debug it using print or breakpoint().

# Exercise 3:
# Explore pytest and write some tests with it.

# --- Save user exercises to webapp/routes.py ---

def save_exercises_to_webapp():
    exercises_code = "\n# --- Chapter 11 User Exercises ---\n"

    # Exercise 1: /test-request-handler
    exercises_code += (
        "def test_request_handler_route():\n"
        "    # Simulate a test for the request handler\n"
        "    routes = {'/': lambda: 'home'}\n"
        "    def handle_request(url):\n"
        "        if (handler := routes.get(url)) is not None:\n"
        "            return handler()\n"
        "        else:\n"
        "            return '404 Not Found'\n"
        "    result = handle_request('/')\n"
        "    return f'Test result: {result == \"home\"}'\n"
        "routes['/test-request-handler'] = test_request_handler_route\n\n"
    )

    # Exercise 2: /debug-bug
    exercises_code += (
        "def debug_bug_route():\n"
        "    # Simulate debugging a bug\n"
        "    try:\n"
        "        x = 1 / 0\n"
        "    except ZeroDivisionError:\n"
        "        return 'Debugged ZeroDivisionError!'\n"
        "    return 'No error.'\n"
        "routes['/debug-bug'] = debug_bug_route\n\n"
    )

    # Exercise 3: /pytest-demo
    exercises_code += (
        "def pytest_demo_route():\n"
        "    # Simulate a pytest test\n"
        "    def add(a, b):\n"
        "        return a + b\n"
        "    assert add(2, 2) == 4\n"
        "    return 'Pytest-style test passed.'\n"
        "routes['/pytest-demo'] = pytest_demo_route\n\n"
    )

    # Append or update the exercises in webapp/routes.py
    with open("webapp/routes.py", "r") as f:
        content = f.read()

    marker = "# --- Chapter 11 User Exercises ---"
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

    print("Saved your Chapter 11 exercises to webapp/routes.py!")

if __name__ == "__main__":
    save_exercises_to_webapp()
