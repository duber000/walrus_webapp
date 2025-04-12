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
        if (resp := await client.get(url)).status_code == 200:
            return resp.json()
        else:
            resp.raise_for_status()

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

# --- Save user exercises to webapp/routes.py ---

def save_exercises_to_webapp():
    exercises_code = "\n# --- Chapter 21 User Exercises ---\n"

    # Exercise 1: async error handling
    exercises_code += (
        "import httpx\n"
        "async def fetch_users_async_safe():\n"
        "    url = 'https://jsonplaceholder.typicode.com/users'\n"
        "    try:\n"
        "        async with httpx.AsyncClient() as client:\n"
        "            resp = await client.get(url)\n"
        "            resp.raise_for_status()\n"
        "            return resp.json()\n"
        "    except Exception:\n"
        "        return None\n\n"
    )

    # Exercise 2: query params for API
    exercises_code += (
        "async def fetch_posts_by_user(user_id):\n"
        "    url = 'https://jsonplaceholder.typicode.com/posts'\n"
        "    params = {'userId': user_id}\n"
        "    async with httpx.AsyncClient() as client:\n"
        "        resp = await client.get(url, params=params)\n"
        "        resp.raise_for_status()\n"
        "        return resp.json()\n\n"
    )

    # Exercise 3: integrate into webapp route
    exercises_code += (
        "async def posts_by_user_route(scope, receive, send):\n"
        "    from urllib.parse import parse_qs\n"
        "    query_string = scope.get('query_string', b'').decode()\n"
        "    params = parse_qs(query_string)\n"
        "    user_id = params.get('userId', ['1'])[0]\n"
        "    posts = await fetch_posts_by_user(user_id)\n"
        "    import json\n"
        "    body = json.dumps(posts).encode()\n"
        "    headers = [(b'content-type', b'application/json')]\n"
        "    await send({'type': 'http.response.start', 'status': 200, 'headers': headers})\n"
        "    await send({'type': 'http.response.body', 'body': body})\n"
        "routes['/posts-by-user'] = posts_by_user_route\n\n"
    )

    # Exercise 4: fetch multiple user lists concurrently
    exercises_code += (
        "import asyncio\n"
        "async def fetch_multiple_users():\n"
        "    urls = [\n"
        "        'https://jsonplaceholder.typicode.com/users',\n"
        "        'https://jsonplaceholder.typicode.com/users?userId=2'\n"
        "    ]\n"
        "    async with httpx.AsyncClient() as client:\n"
        "        results = await asyncio.gather(*(client.get(url) for url in urls))\n"
        "        return [resp.json() for resp in results]\n\n"
    )

    # Exercise 5: timeout handling
    exercises_code += (
        "async def fetch_with_timeout(url, timeout=2.0):\n"
        "    try:\n"
        "        async with httpx.AsyncClient(timeout=timeout) as client:\n"
        "            resp = await client.get(url)\n"
        "            resp.raise_for_status()\n"
        "            return resp.json()\n"
        "    except httpx.TimeoutException:\n"
        "        return {'error': 'Request timed out'}\n"
        "    except Exception as e:\n"
        "        return {'error': str(e)}\n\n"
    )

    # Exercise 6: post multiple new posts concurrently
    exercises_code += (
        "async def post_multiple_posts(posts):\n"
        "    url = 'https://jsonplaceholder.typicode.com/posts'\n"
        "    async with httpx.AsyncClient() as client:\n"
        "        tasks = [client.post(url, json=post) for post in posts]\n"
        "        results = await asyncio.gather(*tasks)\n"
        "        return [resp.json() for resp in results]\n\n"
    )

    # Append or update the exercises in webapp/routes.py
    with open('webapp/routes.py', 'r') as f:
        content = f.read()

    marker = '# --- Chapter 21 User Exercises ---'
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

    print("Saved your Chapter 21 exercises to webapp/routes.py!")

if __name__ == "__main__":
    save_exercises_to_webapp()
