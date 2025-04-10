# Chapter 12: Async Programming and Async ORM Integration

# This chapter introduces async/await, event loops, and async database access with Tortoise ORM.

import asyncio
from tortoise import Tortoise, fields, models

# --- Async Basics ---

async def say_hello():
    print("Hello ...")
    await asyncio.sleep(1)
    print("... World!")

asyncio.run(say_hello())

# --- Async Tortoise ORM Setup ---

class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    email = fields.CharField(max_length=100, unique=True)
    is_active = fields.BooleanField(default=True)

    def __str__(self):
        return self.username

async def init_db():
    await Tortoise.init(
        db_url="sqlite://db.sqlite3",
        modules={"models": ["chapter12_async_programming"]}
    )
    await Tortoise.generate_schemas()

async def create_and_query_users():
    # Create a user
    user, created = await User.get_or_create(
        username="alice",
        defaults={"email": "alice@example.com", "is_active": True}
    )
    print(f"User: {user}, created: {created}")

    # Query all users
    users = await User.all()
    for u in users:
        print("User in DB:", u)

async def main():
    await init_db()
    await create_and_query_users()
    await Tortoise.close_connections()

print("\n--- Running async DB example ---")
asyncio.run(main())

# --- Mini Web Framework: Async route example ---

async def async_user_list():
    users = await User.all()
    return ", ".join([u.username for u in users])

print("\n--- Async ORM integration complete! ---")

# In the next chapters, you can add async routes to your web server.
