# Chapter 21: Consuming External APIs with Requests and HTTPX

# This chapter teaches how to read from and write to external APIs,
# both synchronously (requests) and asynchronously (httpx).

import asyncio
import json
import requests
import httpx

# --- Synchronous API calls with requests ---

def fetch_users_sync():
    """
    Fetch users from an external API synchronously.

    Returns:
        list: List of user dicts.
    """
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def create_post_sync(title, body, user_id):
    """
    Create a post via an external API synchronously.

    Args:
        title (str): Post title.
        body (str): Post content.
        user_id (int): User ID.

    Returns:
        dict: Created post data.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {"title": title, "body": body, "userId": user_id}
    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()

# --- Asynchronous API calls with httpx ---

async def fetch_users_async():
    """
    Fetch users from an external API asynchronously.

    Returns:
        list: List of user dicts.
    """
    url = "https://jsonplaceholder.typicode.com/users"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.json()

async def create_post_async(title, body, user_id):
    """
    Create a post via an external API asynchronously.

    Args:
        title (str): Post title.
        body (str): Post content.
        user_id (int): User ID.

    Returns:
        dict: Created post data.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {"title": title, "body": body, "userId": user_id}
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload)
        response.raise_for_status()
        return response.json()

# --- Example usage ---

def demo_sync():
    print("Fetching users synchronously...")
    users = fetch_users_sync()
    print("Got", len(users), "users.")
    print("Creating a post synchronously...")
    post = create_post_sync("Hello", "This is a sync post", 1)
    print("Created post:", post)

async def demo_async():
    print("Fetching users asynchronously...")
    users = await fetch_users_async()
    print("Got", len(users), "users.")
    print("Creating a post asynchronously...")
    post = await create_post_async("Hello", "This is an async post", 1)
    print("Created post:", post)

if __name__ == "__main__":
    demo_sync()
    asyncio.run(demo_async())

# --- Exercises ---

# Exercise 1:
# Modify the async functions to handle API errors gracefully and return None on failure.

# Exercise 2:
# Add query parameters to filter API results (e.g., fetch posts by userId).

# Exercise 3:
# Integrate these API calls into your web framework routes.

# --- Beginner Async Exercises ---

# Exercise 4:
# Write an async function that fetches multiple user lists concurrently using asyncio.gather().

# Exercise 5:
# Add timeout handling to your async API calls with httpx.

# Exercise 6:
# Create an async function that posts multiple new posts concurrently and collects their responses.
