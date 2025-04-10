# Python Web Framework for learning Python with the Walrus Operator

## Purpose

Step by step plan for learning Python, broken into incremental chapters. Each chapter builds on the previous, culminating in a web framework that heavily uses functional programming, multithreading, GPU parallelism, async programming, and API integration.

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
uv run python webapp/server.py
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
├── ... (other chapters)
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
- The project builds a Python learning path culminating in a mini async web framework with GPU acceleration and API integration.

---

## Resources

- [uv documentation](https://github.com/astral-sh/uv)
- [PEP 621 pyproject.toml guide](https://packaging.python.org/en/latest/specifications/declaring-project-metadata/)

