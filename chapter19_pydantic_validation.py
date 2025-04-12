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

# --- Save user exercises to webapp/routes.py ---

def save_exercises_to_webapp():
    exercises_code = "\n# --- Chapter 19 User Exercises ---\n"

    # Exercise 1: ProductDTO
    exercises_code += (
        "from pydantic import BaseModel\n"
        "class ProductDTO(BaseModel):\n"
        "    id: int\n"
        "    name: str\n"
        "    price: float\n"
        "    in_stock: bool = True\n\n"
    )

    # Exercise 2: OrderDTO
    exercises_code += (
        "from typing import List\n"
        "class OrderDTO(BaseModel):\n"
        "    products: List[ProductDTO]\n"
        "    total_price: float\n\n"
    )

    # Exercise 3: /parse-product
    exercises_code += (
        "def parse_product_route(json_str):\n"
        "    try:\n"
        "        product = ProductDTO.parse_raw(json_str)\n"
        "        return f'Parsed: {product}'\n"
        "    except Exception as e:\n"
        "        return f'Validation error: {e}'\n"
        "routes['/parse-product'] = parse_product_route\n\n"
    )

    # Append or update the exercises in webapp/routes.py
    with open('webapp/routes.py', 'r') as f:
        content = f.read()

    marker = '# --- Chapter 19 User Exercises ---'
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

    print("Saved your Chapter 19 exercises to webapp/routes.py!")

if __name__ == "__main__":
    save_exercises_to_webapp()

# --- Summary ---

# Pydantic helps you write safer, cleaner code by:
# - Validating data at runtime
# - Parsing and converting types automatically
# - Providing clear error messages
# - Making it easy to serialize/deserialize data
# - Integrating well with async frameworks like FastAPI

# It's a great complement to your async web framework and ORM models!
