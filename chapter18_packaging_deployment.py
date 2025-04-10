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
