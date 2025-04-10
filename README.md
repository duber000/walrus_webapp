# Python Web Framework for learning Python with the Walrus Operator

## Purpose

A step-by-step plan for learning Python, broken into incremental chapters. Each chapter builds on the previous, culminating in a web framework that heavily uses functional programming, multithreading, GPU parallelism, async programming, and API integration — all while showcasing the walrus operator (`:=`).

---

## Chapter Overview

| Chapter | Topic | Description |
|---------|----------------------------|--------------------------------------------------------------|
| **1**   | Variables & Data Types    | Introduces Python variables, strings, numbers, lists, dicts, sets, and basic printing. |
| **2**   | Control Flow              | `if`, `elif`, `else`, loops, logical operators, pattern matching, and first use of the walrus operator. |
| **3**   | Functions                 | Defining functions, parameters, return values, nested functions, and routing logic as functions. |
| **4**   | Functional Programming    | Lambdas, `map`, `filter`, `reduce`, and more walrus operator examples. |
| **5**   | Multithreading            | Using `threading` to handle multiple requests concurrently in the mini web framework. |
| **6**   | GPU Parallelism           | Accelerate array computations with Numba and CUDA, and integrate GPU routes. |
| **7**   | Modules & File I/O        | Organize code into modules, read/write files, and intro to ORM models. |
| **8**   | Error Handling            | `try`/`except`, raising exceptions, graceful error handling in the framework. |
| **9**   | Object-Oriented Programming | Classes, inheritance, dataclasses, and an OOP design for the framework. |
| **10**  | Building a Web Server     | Create a simple HTTP server with `http.server` and route handling. |
| **11**  | Testing & Debugging       | `assert`, `unittest`, debugging tips, and writing tests for the framework. |
| **12**  | Async Programming & ORM   | `async`/`await`, event loops, async database access with Tortoise ORM. |
| **13**  | HTTP, REST & JSON         | HTTP methods, status codes, REST API design, JSON serialization. |
| **14**  | Requests, Responses, Middleware | Request/Response classes, middleware pattern, and chaining. |
| **15**  | Routing & Decorators      | Dynamic routing with regex, decorators for route registration. |
| **16**  | Security Essentials       | Input validation, password hashing, tokens, authorization, CORS. |
| **17**  | Templates & Static Files  | Jinja2 templates, serving static files, and template inheritance. |
| **18**  | Packaging & Deployment    | `pyproject.toml`, Docker, ASGI servers, deployment options. |
| **19**  | Data Validation with Pydantic | Pydantic models for validation, nested models, serialization. |
| **20**  | Async API Client          | Using `httpx` to fetch external APIs asynchronously, with ASGI integration. |
| **21**  | Sync & Async API Clients  | Using `requests` and `httpx` for API calls, error handling, concurrency. |
| **+**   | PyTorch Integration       | Async GPU inference with PyTorch, integrated into the web app. |

---

## Project Setup with **uv**

This project uses [**uv**](https://github.com/astral-sh/uv) for **fast, modern Python project management**.

### Initialize a new project (if you haven't yet)

```bash
uv init
```

This creates:

- `pyproject.toml` (project metadata and dependencies)
- `.python-version` (default Python version)
- `README.md`
- `main.py` (starter script)

### Adding dependencies

Add all required packages with:

```bash
uv add tortoise-orm numba numpy jinja2 pydantic uvicorn torch httpx requests
```

You can add more packages later with `uv add <package>`.

### Sync environment

`uv` automatically syncs your environment when running commands, but you can also do it manually:

```bash
uv sync
```

### Running your app

Run any script or command inside the project environment:

```bash
uv run webapp/server.py
```

Or, for example, to start the ASGI server with uvicorn:

```bash
uv run -- uvicorn webapp.server:app --reload
```

### Managing dependencies

- **Add**: `uv add <package>`
- **Remove**: `uv remove <package>`
- **Upgrade**: `uv lock --upgrade-package <package>`

### Building distributions

Build wheels and source distributions:

```bash
uv build
```

---

## Project structure

After setup, your project will look like:

```
.
├── .python-version
├── pyproject.toml
├── uv.lock
├── .venv/
├── README.md
├── main.py
├── webapp/
│   ├── __init__.py
│   ├── server.py
│   ├── routes.py
│   ├── models.py
│   ├── utils.py
│   └── torch_model.py
├── chapter1_variables.py
├── chapter2_control_flow.py
├── chapter3_functions.py
├── chapter4_functional_programming.py
├── chapter5_multithreading.py
├── chapter6_gpu_parallelism.py
├── chapter7_modules_fileio.py
├── chapter8_error_handling.py
├── chapter9_oop.py
├── chapter10_web_server.py
├── chapter11_testing.py
├── chapter12_async_programming.py
├── chapter13_http_rest.py
├── chapter14_request_response.py
├── chapter15_routing_decorators.py
├── chapter16_security.py
├── chapter17_templates_static.py
├── chapter18_packaging_deployment.py
├── chapter19_pydantic_validation.py
├── chapter20_external_api.py
├── chapter21_api_client.py
```

---

## API Client Chapter

### Chapter 21: Consuming External APIs

Learn how to read from and write to external APIs using:

- **requests** (sync)
- **httpx** (async)

Example routes:

- `GET /external-users-sync` — fetch users synchronously
- `GET /external-users-async` — fetch users asynchronously
- `POST /create-post-async` — create a post asynchronously (send JSON: `{"title": "...", "body": "...", "userId": 1}`)

Test with:

```bash
curl http://localhost:8000/external-users-sync
curl http://localhost:8000/external-users-async
curl -X POST -H "Content-Type: application/json" -d '{"title":"Test","body":"Hello","userId":1}' http://localhost:8000/create-post-async
```

---

## Learning Path & Branching Strategy

- Each chapter is developed in its own branch, starting from `main`.
- Branches are named sequentially, e.g., `chapter1-variables`, `chapter2-control-flow`, etc.
- You can checkout any chapter branch to learn that topic in isolation.
- Optionally, chapters can be merged back into `main` after stabilization.

---

## Summary

- This project is managed with **uv**.
- Dependencies are declared in **pyproject.toml** and locked in **uv.lock**.
- Use `uv add` to add packages, `uv run` to run commands, and `uv build` to build distributions.
- The project builds a Python learning path culminating in a mini async web framework with GPU acceleration, API integration, and plenty of walrus operator usage!

