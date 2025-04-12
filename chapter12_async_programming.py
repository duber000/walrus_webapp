# Chapter 12: Async Programming and Async ORM Integration

# This chapter introduces async/await, event loops, and async database access with Tortoise ORM.

import asyncio
from dataclasses import dataclass
from tortoise import Tortoise, fields, models

# --- Async Basics ---

# This is an example of an async function.
# 'await' pauses execution until the async operation completes.
async def say_hello():
    print("Hello ...")
    await asyncio.sleep(1)
    print("... World!")

# Run the async function using asyncio's event loop.
asyncio.run(say_hello())

# --- Async Tortoise ORM Setup ---

class User(models.Model):
    """
    Tortoise ORM User model representing a user in the database.
    """
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    email = fields.CharField(max_length=100, unique=True)
    is_active = fields.BooleanField(default=True)

    def __str__(self):
        return self.username

# We'll use a dataclass as a Data Transfer Object (DTO) to convert ORM model instances
# into plain data containers, which are easier to serialize or pass to other parts of the app.
@dataclass
class UserDTO:
    """
    Data Transfer Object for User model.
    """
    id: int
    username: str
    email: str
    is_active: bool

    @classmethod
    def from_model(cls, user: "User") -> "UserDTO":
        """
        Convert a User ORM model instance to a UserDTO.

        Args:
            user (User): The ORM User instance.

        Returns:
            UserDTO: The data transfer object.
        """
        return cls(
            id=user.id,
            username=user.username,
            email=user.email,
            is_active=user.is_active
        )

async def init_db():
    """
    Initialize the Tortoise ORM database connection and generate schemas.
    """
    await Tortoise.init(
        db_url="sqlite://db.sqlite3",
        modules={"models": ["chapter12_async_programming"]}
    )
    await Tortoise.generate_schemas()

async def create_and_query_users():
    """
    Create a sample user and query all users from the database.
    """
    # Create a user if not exists
    user, created = await User.get_or_create(
        username="alice",
        defaults={"email": "alice@example.com", "is_active": True}
    )
    print(f"User: {user}, created: {created}")

    # Query all users
    users = await User.all()
    for u in users:
        dto = UserDTO.from_model(u)
        print("User DTO:", dto)

async def main():
    """
    Main async function to initialize DB, create/query users, and close connections.
    """
    await init_db()
    await create_and_query_users()
    await Tortoise.close_connections()

print("\n--- Running async DB example ---")
asyncio.run(main())

# --- Mini Web Framework: Async route example ---

async def async_user_list():
    """
    Example async route handler that returns a comma-separated list of usernames.
    """
    if (users := await User.all()):
        dtos = [UserDTO.from_model(u) for u in users]
        return ", ".join([dto.username for dto in dtos])
    else:
        return "No users found."

print("\n--- Async ORM integration complete! ---")

# In the next chapters, you can add async routes to your web server.

# --- Beginner Async Exercises ---

# Exercise 1:
# Write an async function that waits 2 seconds and then prints "Done waiting".

# Exercise 2:
# Modify `create_and_query_users()` to create multiple users asynchronously in a loop.

# Exercise 3:
# Write an async function that fetches data from two APIs concurrently using asyncio.gather().

# --- Save user exercises to webapp/routes.py ---

def save_exercises_to_webapp():
    exercises_code = "\n# --- Chapter 12 User Exercises ---\n"

    # Exercise 1: /async-wait
    exercises_code += (
        "import asyncio\n"
        "async def async_wait_route():\n"
        "    await asyncio.sleep(2)\n"
        "    return 'Done waiting'\n"
        "routes['/async-wait'] = async_wait_route\n\n"
    )

    # Exercise 2: /create-multi-users
    exercises_code += (
        "async def create_multi_users_route():\n"
        "    from tortoise import Tortoise, fields, models\n"
        "    class User(models.Model):\n"
        "        id = fields.IntField(pk=True)\n"
        "        username = fields.CharField(max_length=50, unique=True)\n"
        "        email = fields.CharField(max_length=100, unique=True)\n"
        "        is_active = fields.BooleanField(default=True)\n"
        "    await Tortoise.init(db_url='sqlite://db.sqlite3', modules={'models': ['webapp.models']})\n"
        "    await Tortoise.generate_schemas()\n"
        "    for i in range(3):\n"
        "        await User.get_or_create(username=f'user{i}', defaults={'email': f'user{i}@example.com', 'is_active': True})\n"
        "    users = await User.all()\n"
        "    return ', '.join([u.username for u in users])\n"
        "routes['/create-multi-users'] = create_multi_users_route\n\n"
    )

    # Exercise 3: /gather-apis
    exercises_code += (
        "import asyncio\n"
        "async def gather_apis_route():\n"
        "    async def fake_api(name):\n"
        "        await asyncio.sleep(0.5)\n"
        "        return f'{name} result'\n"
        "    results = await asyncio.gather(fake_api('api1'), fake_api('api2'))\n"
        "    return ', '.join(results)\n"
        "routes['/gather-apis'] = gather_apis_route\n\n"
    )

    # Append or update the exercises in webapp/routes.py
    with open('webapp/routes.py', 'r') as f:
        content = f.read()

    marker = '# --- Chapter 12 User Exercises ---'
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

    print("Saved your Chapter 12 exercises to webapp/routes.py!")

if __name__ == "__main__":
    save_exercises_to_webapp()
