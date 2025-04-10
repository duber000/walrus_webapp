# Chapter 11: Testing and Debugging

# This chapter introduces writing tests and debugging Python code.

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

if __name__ == "__main__":
    unittest.main()

# --- Debugging tips ---

# Use print() statements to trace values.
# Use breakpoints in IDEs or pdb module:
# import pdb; pdb.set_trace()

# --- Exercises ---

# Exercise 1:
# Write tests for your mini web framework's request handler.

# Exercise 2:
# Intentionally introduce a bug and debug it using print or pdb.

# Exercise 3:
# Explore pytest and write some tests with it.
