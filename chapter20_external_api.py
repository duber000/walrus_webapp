
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

# --- Beginner Async Exercises ---

# Exercise 4:
# Write an async function that fetches two different URLs concurrently and prints their status codes.

# Exercise 5:
# Add error handling to your async API calls to print a friendly message if the request fails.

# Exercise 6:
# Create an async function that retries a failed API call up to 3 times with a delay.

# --- Save user exercises to webapp/routes.py ---

def save_exercises_to_webapp():
    exercises_code = "\n# --- Chapter 20 User Exercises ---\n"

    # Exercise 1: fetch_users_async with error handling
    exercises_code += (
        "import httpx\n"
        "import asyncio\n"
        "async def fetch_users_async_safe():\n"
        "    url = 'https://jsonplaceholder.typicode.com/users'\n"
        "    try:\n"
        "        async with httpx.AsyncClient() as client:\n"
        "            response = await client.get(url)\n"
        "            response.raise_for_status()\n"
        "            return response.json()\n"
        "    except Exception:\n"
        "        return []\n\n"
    )

    # Exercise 2: async POST to external API
    exercises_code += (
        "async def post_user_async(user_data):\n"
        "    url = 'https://jsonplaceholder.typicode.com/users'\n"
        "    try:\n"
        "        async with httpx.AsyncClient() as client:\n"
        "            response = await client.post(url, json=user_data)\n"
        "            response.raise_for_status()\n"
        "            return response.json()\n"
        "    except Exception as e:\n"
        "        return {'error': str(e)}\n\n"
    )

    # Exercise 3: ASGI route for POST user
    exercises_code += (
        "async def post_user_route_async(scope, receive, send):\n"
        "    assert scope['type'] == 'http'\n"
        "    body = b''\n"
        "    while True:\n"
        "        message = await receive()\n"
        "        body += message.get('body', b'')\n"
        "        if not message.get('more_body', False):\n"
        "            break\n"
        "    import json\n"
        "    try:\n"
        "        user_data = json.loads(body.decode())\n"
        "    except Exception:\n"
        "        user_data = {}\n"
        "    result = await post_user_async(user_data)\n"
        "    response_body = json.dumps(result).encode()\n"
        "    headers = [(b'content-type', b'application/json')]\n"
        "    await send({'type': 'http.response.start', 'status': 201, 'headers': headers})\n"
        "    await send({'type': 'http.response.body', 'body': response_body})\n\n"
        "routes['/post-user-async'] = post_user_route_async\n\n"
    )

    # Exercise 4: fetch two URLs concurrently
    exercises_code += (
        "async def fetch_two_urls():\n"
        "    urls = [\n"
        "        'https://jsonplaceholder.typicode.com/users',\n"
        "        'https://jsonplaceholder.typicode.com/posts'\n"
        "    ]\n"
        "    async with httpx.AsyncClient() as client:\n"
        "        results = await asyncio.gather(*(client.get(url) for url in urls))\n"
        "        return [resp.status_code for resp in results]\n\n"
    )

    # Exercise 5: error handling in async API calls
    exercises_code += (
        "async def safe_get(url):\n"
        "    try:\n"
        "        async with httpx.AsyncClient() as client:\n"
        "            resp = await client.get(url)\n"
        "            resp.raise_for_status()\n"
        "            return resp.json()\n"
        "    except Exception as e:\n"
        "        return {'error': f'Failed to fetch {url}: {e}'}\n\n"
    )

    # Exercise 6: retry async API call
    exercises_code += (
        "async def retry_get(url, retries=3, delay=0.5):\n"
        "    for attempt in range(retries):\n"
        "        try:\n"
        "            async with httpx.AsyncClient() as client:\n"
        "                resp = await client.get(url)\n"
        "                resp.raise_for_status()\n"
        "                return resp.json()\n"
        "        except Exception as e:\n"
        "            if attempt == retries - 1:\n"
        "                return {'error': f'Failed after {retries} attempts: {e}'}\n"
        "            await asyncio.sleep(delay)\n\n"
    )

    # Append or update the exercises in webapp/routes.py
    with open('webapp/routes.py', 'r') as f:
        content = f.read()

    marker = '# --- Chapter 20 User Exercises ---'
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

    print("Saved your Chapter 20 exercises to webapp/routes.py!")

if __name__ == "__main__":
    save_exercises_to_webapp()
