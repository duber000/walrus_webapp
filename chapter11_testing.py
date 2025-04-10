# Chapter 11: Testing and Debugging

# This chapter introduces writing tests and debugging Python code.

from dataclasses import dataclass

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

    # Exercise 1: tests for request handler (simulate output)
    exercises_code += (
        "def exercise11_1():\n"
        "    return 'Wrote tests for request handler.'\n\n"
    )

    # Exercise 2: debugged a bug (simulate output)
    exercises_code += (
        "def exercise11_2():\n"
        "    return 'Debugged a bug using print and breakpoint.'\n\n"
    )

    # Exercise 3: explored pytest (simulate output)
    exercises_code += (
        "def exercise11_3():\n"
        "    return 'Explored pytest and wrote some tests.'\n\n"
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
