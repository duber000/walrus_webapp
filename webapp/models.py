# webapp/models.py
# Tortoise ORM models and initialization

from tortoise import Tortoise, fields, models, run_async

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
        modules={"models": ["webapp.models"]}
    )
    await Tortoise.generate_schemas()

async def create_sample_user():
    user, created = await User.get_or_create(
        username="alice",
        defaults={"email": "alice@example.com", "is_active": True}
    )
    print(f"User: {user}, created: {created}")

if __name__ == "__main__":
    async def run():
        await init_db()
        await create_sample_user()
        users = await User.all()
        for user in users:
            print(user)
        await Tortoise.close_connections()

    run_async(run())
