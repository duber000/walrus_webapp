# Python Web Framework for learning Python with the Walrus Operator

## Purpose
Step by step plan for learning Python, broken into incremental chapters. Each chapter builds on the previous, culminating in a web framework that heavily uses functional programming, multithreading, and GPU parallelism.

## Setup

This project uses several third-party libraries for async programming, GPU acceleration, templating, and validation.

### Install dependencies

```bash
pip install tortoise-orm numba numpy jinja2 pydantic uvicorn torch httpx requests
```

- **tortoise-orm**: async ORM for database models
- **numba**: JIT compiler for Python, used for GPU acceleration
- **numpy**: numerical arrays, used with Numba
- **jinja2**: HTML templating engine
- **pydantic**: data validation and parsing
- **uvicorn**: ASGI server for running async web apps
- **torch**: PyTorch deep learning framework, used for ML inference
- **httpx**: async HTTP client for calling external APIs
- **requests**: synchronous HTTP client for calling external APIs

Alternatively, you can add these to your `pyproject.toml` or `requirements.txt`.

---

## Learning Path & Branching Strategy

### How to use this repository

- Each chapter is developed in its own branch, starting from `main`.
- Branches are named sequentially, e.g., `chapter1-variables`, `chapter2-control-flow`, etc.
- You can checkout any chapter branch to learn that topic in isolation.
- Optionally, chapters can be merged back into `main` after stabilization.

### Chapters

| Chapter | Branch | Description |
|---------|--------|-------------|
| **Chapter 1: Variables** | [`chapter1-variables`](https://github.com/yourrepo/tree/chapter1-variables) | Learn about variables and data types in Python. |
| **Chapter 2: Control Flow** | [`chapter2-control-flow`](https://github.com/yourrepo/tree/chapter2-control-flow) | Learn about if statements, loops, and control structures. |
| **Chapter 3: Functions** | [`chapter3-functions`](https://github.com/yourrepo/tree/chapter3-functions) | Learn how to write and use functions. |
| **Chapter 4: Functional Programming** | [`chapter4-functional-programming`](https://github.com/yourrepo/tree/chapter4-functional-programming) | Learn about map, filter, reduce, lambdas, and the Walrus operator. |
| **Chapter 5: Multithreading** | [`chapter5-multithreading`](https://github.com/yourrepo/tree/chapter5-multithreading) | Learn how to write multithreaded Python programs. |
| **Chapter 6: GPU Parallelism** | [`chapter6-gpu-parallelism`](https://github.com/yourrepo/tree/chapter6-gpu-parallelism) | Learn how to leverage GPU acceleration for parallel computing. |
| **Chapter 7: Modules and File I/O** | [`chapter7-modules-fileio`](https://github.com/yourrepo/tree/chapter7-modules-fileio) | Learn how to organize code into modules and read/write files. |
| **Chapter 8: Error Handling** | [`chapter8-error-handling`](https://github.com/yourrepo/tree/chapter8-error-handling) | Learn how to handle errors and exceptions in Python. |
| **Chapter 9: Object-Oriented Programming** | [`chapter9-oop`](https://github.com/yourrepo/tree/chapter9-oop) | Learn about classes, objects, and OOP concepts. |
| **Chapter 10: Building a Real Web Server** | [`chapter10-web-server`](https://github.com/yourrepo/tree/chapter10-web-server) | Learn how to build a simple HTTP server in Python. |
| **Chapter 11: Testing and Debugging** | [`chapter11-testing`](https://github.com/yourrepo/tree/chapter11-testing) | Learn how to write tests and debug Python code. |

---

## Development Workflow

1. **Start from `main` branch**

2. **Create a branch for the first chapter:**

   ```bash
   git checkout -b chapter1-variables
   ```

3. **Develop chapter content:**

   - Add code examples, exercises, and explanations.
   - Update this `README.md` with chapter details.
   - Commit changes:

     ```bash
     git add .
     git commit -m "Add examples and exercises for Chapter 1: Variables"
     ```

4. **Create the next chapter branch from the previous:**

   ```bash
   git checkout -b chapter2-control-flow
   ```

5. **Repeat for all chapters**

6. **Merge strategy:**

   - Optionally merge each chapter back into `main` after completion.
   - Or keep branches separate for learners to explore individually.

---

## Goal

By following this incremental approach, learners will gradually build a deep understanding of Python, functional programming, concurrency, and GPU parallelism, culminating in a powerful, modern web framework.

