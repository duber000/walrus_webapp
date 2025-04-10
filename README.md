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

## Setup (with [uv](https://github.com/astral-sh/uv))

```bash
uv init
uv add tortoise-orm numba numpy jinja2 pydantic uvicorn torch httpx requests
uv run -- uvicorn webapp.server:app --reload
```

---

## Usage

- Visit `/`, `/about`, `/greet`, `/squares`, `/file-content`, `/user`, `/external-users-sync`, `/external-users-async`
- POST JSON to `/predict` or `/create-post-async`
- See the walrus operator in action throughout the codebase!

---

## Why "Walrus Framework"?

Because this project **embraces** Python's assignment expression (`:=`) everywhere — in routing, async loops, API calls, and more 

