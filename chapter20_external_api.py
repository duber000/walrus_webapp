
# Chapter 20: Consuming External APIs (Async with HTTPX)

# This chapter introduces how to fetch data asynchronously from external APIs using `httpx`.
# It also shows how to integrate async API calls into your ASGI-compatible web framework.

import httpx
import json

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

async def external_users_route_async(scope, receive, send):
    """
    ASGI route handler that fetches users from an external API and returns JSON response.

    This demonstrates how to:
    - Receive an ASGI HTTP request
    - Call an async HTTP client (`httpx`) to fetch data
    - Send a JSON response back to the client
    """
    users = await fetch_users_async()
    body = json.dumps(users).encode()

    headers = [(b"content-type", b"application/json")]

    await send({
        "type": "http.response.start",
        "status": 200,
        "headers": headers
    })
    await send({
        "type": "http.response.body",
        "body": body
    })

# --- Exercises ---

# Exercise 1:
# Modify `fetch_users_async()` to handle network errors gracefully and return an empty list on failure.

# Exercise 2:
# Add a new async function to POST data to an external API (e.g., create a new user).

# Exercise 3:
# Integrate this API call into your web framework with a new ASGI route.
