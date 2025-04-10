# Chapter 19: Data Validation with Pydantic

# This chapter introduces Pydantic, a powerful library for data validation and settings management.
# Pydantic models combine the benefits of dataclasses with runtime validation and parsing.

from pydantic import BaseModel, EmailStr, ValidationError, constr
from typing import Optional, List

# --- Basic Pydantic Model ---

class UserDTO(BaseModel):
    """
    User Data Transfer Object with validation.
    """
    id: int
    username: constr(min_length=3, max_length=20)
    email: EmailStr
    is_active: bool = True

# Pydantic automatically validates and converts data types
try:
    user = UserDTO(id="123", username="alice", email="alice@example.com")
    print("UserDTO created:", user)
except ValidationError as e:
    print("Validation error:", e)

# Invalid email example
try:
    bad_user = UserDTO(id=1, username="bob", email="not-an-email")
except ValidationError as e:
    print("Validation error:", e)

# --- Nested Models ---

class PostDTO(BaseModel):
    id: int
    title: str
    content: str
    author: UserDTO

post = PostDTO(
    id=1,
    title="Hello World",
    content="This is my first post.",
    author=user
)
print("PostDTO with nested UserDTO:", post)

# --- Optional Fields and Default Values ---

class CommentDTO(BaseModel):
    id: int
    content: str
    author: Optional[UserDTO] = None

comment = CommentDTO(id=1, content="Nice post!")
print("CommentDTO with optional author:", comment)

# --- List of Models ---

class BlogDTO(BaseModel):
    title: str
    posts: List[PostDTO]

blog = BlogDTO(title="My Blog", posts=[post])
print("BlogDTO with list of posts:", blog)

# --- Serialization ---

print("UserDTO as dict:", user.dict())
print("UserDTO as JSON:", user.json())

# --- Integration with REST APIs ---

# You can use Pydantic models to parse incoming JSON requests
# and to serialize responses, ensuring data is valid and well-structured.

# --- Exercises ---

# Exercise 1:
# Define a Pydantic model for a Product with fields: id (int), name (str), price (float), in_stock (bool, default True).

# Exercise 2:
# Create a nested OrderDTO with a list of ProductDTOs and a total_price field.

# Exercise 3:
# Parse a JSON string into your ProductDTO and handle validation errors.

# --- Summary ---

# Pydantic helps you write safer, cleaner code by:
# - Validating data at runtime
# - Parsing and converting types automatically
# - Providing clear error messages
# - Making it easy to serialize/deserialize data
# - Integrating well with async frameworks like FastAPI

# It's a great complement to your async web framework and ORM models!
