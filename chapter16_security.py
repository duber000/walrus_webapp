# Chapter 16: Security Essentials

# This chapter introduces input validation, authentication, authorization, and CORS.

import hashlib
import hmac

# --- Input Validation ---

def is_valid_username(username):
    """
    Validate that the username is alphanumeric and between 3 and 20 characters.

    Args:
        username (str): The username to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    return username.isalnum() and 3 <= len(username) <= 20

print("Valid username 'alice':", is_valid_username("alice"))
print("Invalid username 'a!':", is_valid_username("a!"))

# --- Password Hashing ---

def hash_password(password, salt="somesalt"):
    """
    Hash a password with a salt using SHA-256.

    Args:
        password (str): The plaintext password.
        salt (str): The salt string.

    Returns:
        str: The hexadecimal hash.
    """
    return hashlib.sha256((salt + password).encode()).hexdigest()

hashed = hash_password("secret")
print("Password hash:", hashed)

# --- Token-based Authentication (simplified) ---

SECRET_KEY = "supersecret"

def generate_token(username):
    """
    Generate an HMAC token for a username.

    Args:
        username (str): The username.

    Returns:
        str: The generated token.
    """
    return hmac.new(SECRET_KEY.encode(), username.encode(), "sha256").hexdigest()

def verify_token(username, token):
    """
    Verify that a token matches the username.

    Args:
        username (str): The username.
        token (str): The token to verify.

    Returns:
        bool: True if valid, False otherwise.
    """
    return hmac.compare_digest(generate_token(username), token)

token = generate_token("alice")
print("Token:", token)
print("Verify token:", verify_token("alice", token))

# --- Authorization ---

def is_admin(user_role):
    """
    Check if the user role is 'admin'.

    Args:
        user_role (str): The user's role.

    Returns:
        bool: True if admin, False otherwise.
    """
    return user_role == "admin"

print("Is admin:", is_admin("admin"))
print("Is admin:", is_admin("user"))

# --- CORS Headers ---

def add_cors_headers(response_headers):
    """
    Add Cross-Origin Resource Sharing (CORS) headers to the response.

    Args:
        response_headers (dict): The response headers dictionary.

    Returns:
        dict: The updated headers with CORS info.
    """
    response_headers["Access-Control-Allow-Origin"] = "*"
    response_headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE"
    return response_headers

headers = {}
headers = add_cors_headers(headers)
print("Response headers with CORS:", headers)

# --- Security Concepts ---
# 
# - **Input validation** prevents malicious input from users.
# - **Password hashing** stores passwords securely instead of plaintext.
# - **Tokens** authenticate users without sending passwords each time.
# - **Authorization** restricts access based on user roles.
# - **CORS** controls which domains can access your API.
# 
# These are fundamental to building secure web applications.

# --- Exercises ---

# Exercise 1:
# Improve password hashing with salt and pepper.

# Exercise 2:
# Implement role-based access control for routes.

# Exercise 3:
# Add CSRF protection to POST requests.
