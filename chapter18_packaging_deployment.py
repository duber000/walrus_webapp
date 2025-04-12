# Chapter 18: Packaging, Deployment, and ASGI

# This chapter covers packaging your app, deploying it, and async server interfaces.

# --- Packaging with pyproject.toml ---

# Use Poetry, Hatch, or PDM for modern packaging.
# Example pyproject.toml snippet:
#
# [project]
# name = "mywebapp"
# version = "0.1.0"
# dependencies = ["tortoise-orm", "jinja2", "uvicorn"]
#
# [build-system]
# requires = ["setuptools", "wheel"]
# build-backend = "setuptools.build_meta"

# --- Dockerizing ---

# Example Dockerfile:
#
# FROM python:3.11-slim
# WORKDIR /app
# COPY . .
# RUN pip install -r requirements.txt
# CMD ["uvicorn", "webapp.server:app", "--host", "0.0.0.0", "--port", "8000"]

# --- ASGI Servers ---

# ASGI (Asynchronous Server Gateway Interface) supports async apps.
# Popular servers: uvicorn, hypercorn, daphne.

# Example running with uvicorn:
# uvicorn webapp.server:app --reload

# --- WebSockets (optional) ---

# ASGI supports WebSockets for real-time communication.

# --- Deployment options ---

# - Heroku
# - Fly.io
# - DigitalOcean
# - AWS, GCP, Azure
# - Bare metal with Docker

# --- Exercises ---

# Exercise 1:
# Write a pyproject.toml for your app.

# Exercise 2:
# Create a Dockerfile and build your image.

# Exercise 3:
# Deploy your app to a free hosting platform.

# --- Save user exercises to webapp/routes.py ---

def save_exercises_to_webapp():
    exercises_code = "\n# --- Chapter 18 User Exercises ---\n"

    # Exercise 1: /pyproject-toml
    exercises_code += (
        "def pyproject_toml_route():\n"
        "    return '[project]\\nname = \"mywebapp\"\\nversion = \"0.1.0\"\\ndependencies = [\"tortoise-orm\", \"jinja2\", \"uvicorn\"]'\n"
        "routes['/pyproject-toml'] = pyproject_toml_route\n\n"
    )

    # Exercise 2: /dockerfile
    exercises_code += (
        "def dockerfile_route():\n"
        "    return 'FROM python:3.11-slim\\nWORKDIR /app\\nCOPY . .\\nRUN pip install -r requirements.txt\\nCMD [\"uvicorn\", \"webapp.server:app\", \"--host\", \"0.0.0.0\", \"--port\", \"8000\"]'\n"
        "routes['/dockerfile'] = dockerfile_route\n\n"
    )

    # Exercise 3: /deploy-info
    exercises_code += (
        "def deploy_info_route():\n"
        "    return 'Deployed to Fly.io (or other free hosting platform)'\n"
        "routes['/deploy-info'] = deploy_info_route\n\n"
    )

    # Append or update the exercises in webapp/routes.py
    with open('webapp/routes.py', 'r') as f:
        content = f.read()

    marker = '# --- Chapter 18 User Exercises ---'
    if marker in content:
        pre = content.split(marker)[0]
        post = content.split(marker)[-1]
        post_lines = post.splitlines()
        idx = 0
        for i, line in enumerate(post_lines):
            if line.strip().startswith('# ---'):
                idx = i
                break
        else:
            idx = len(post_lines)
        post = '\n'.join(post_lines[idx:])
        new_content = pre + exercises_code + post
    else:
        new_content = content + '\n' + exercises_code

    with open('webapp/routes.py', 'w') as f:
        f.write(new_content)

    print("Saved your Chapter 18 exercises to webapp/routes.py!")

if __name__ == "__main__":
    save_exercises_to_webapp()
