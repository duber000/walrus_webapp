# Walrus Operator Python Web Framework

A beginner-friendly, incremental Python learning project that builds a mini async web framework — showcasing the walrus operator (`:=`) throughout.

---

## Chapters Overview

- **Chapter 1:** Variables & Data Types
- **Chapter 2:** Control Flow & Walrus Operator
- **Chapter 3:** Functions
- **Chapter 4:** Functional Programming
- **Chapter 5:** Multithreading
- **Chapter 6:** GPU Parallelism (Numba, CUDA)
- **Chapter 7:** Modules & File I/O
- **Chapter 8:** Error Handling
- **Chapter 9:** Object-Oriented Programming
- **Chapter 10:** Building a Web Server
- **Chapter 11:** Testing & Debugging
- **Chapter 12:** Async Programming & ORM
- **Chapter 13:** HTTP, REST & JSON
- **Chapter 14:** Requests, Responses, Middleware
- **Chapter 15:** Routing & Decorators
- **Chapter 16:** Security Essentials
- **Chapter 17:** Templates & Static Files
- **Chapter 18:** Packaging & Deployment
- **Chapter 19:** Data Validation with Pydantic
- **Chapter 20:** Async API Client (httpx)
- **Chapter 21:** Sync & Async API Clients (requests, httpx)
- **PyTorch Integration:** Async GPU inference

---

## How It Works

Each chapter introduces new Python/web concepts and includes exercises that incrementally build the webapp. By completing the exercises and running each chapter as a script, new routes and features are exported to the `webapp/` package (especially `webapp/routes.py`). The webapp grows step by step, and by the end you have a working async web application with modern Python features.

---

## Setup (with [uv](https://github.com/astral-sh/uv))

```bash
uv init
uv add tortoise-orm numba numpy jinja2 pydantic uvicorn torch httpx requests
uv run -- uvicorn webapp.server:app --reload
```

---

## Usage

- Visit routes like `/`, `/about`, `/greet`, `/squares`, `/file-content`, `/user`, `/external-users-sync`, `/external-users-async`, `/predict`, `/external-users`, `/create-post-async`, `/products`, `/admin-only`, `/profile-template`, `/pyproject-toml`, and more.
- POST JSON to `/predict`, `/create-post-async`, `/post-user-async`, etc.
- See the walrus operator in action throughout the codebase!
- Each chapter's `save_exercises_to_webapp()` function will export new routes and features to the webapp.

---

## Features

- **Incremental learning:** Each chapter builds on the last, growing the webapp step by step.
- **Modern Python:** Uses assignment expressions, dataclasses, async/await, type hints, and more.
- **Async ORM:** Tortoise ORM for async database access.
- **REST & API clients:** Both sync and async API consumption (requests, httpx).
- **Testing & validation:** Includes Pydantic, pytest-style tests, and error handling.
- **Templates & static files:** Jinja2 templates and static file serving.
- **Security:** Password hashing, role-based access, CSRF protection.
- **Deployment:** Docker, pyproject.toml, and ASGI server support.
- **PyTorch integration:** Async GPU inference route.

---

## Why "Walrus Framework"?

Because this project **embraces** Python's assignment expression (`:=`) everywhere — in routing, async loops, API calls, and more!

---

## Contributing

Contributions, suggestions, and improvements are welcome! Please open an issue or PR.

---

## License

MIT License

