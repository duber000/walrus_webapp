# Chapter 16: Security Essentials

# This chapter introduces input validation, authentication, authorization, and CORS.

import hashlib
import hmac

# --- Input Validation ---

def is_valid_username(username):
    return username.isalnum() and 3 <= len(username) <= 20

print("Valid username 'alice':", is_valid_username("alice"))
print("Invalid username 'a!':", is_valid_username("a!"))

# --- Password Hashing ---

def hash_password(password, salt="somesalt"):
    return hashlib.sha256((salt + password).encode()).hexdigest()

hashed = hash_password("secret")
print("Password hash:", hashed)

# --- Token-based Authentication (simplified) ---

SECRET_KEY = "supersecret"

def generate_token(username):
    return hmac.new(SECRET_KEY.encode(), username.encode(), "sha256").hexdigest()

def verify_token(username, token):
    return hmac.compare_digest(generate_token(username), token)

token = generate_token("alice")
print("Token:", token)
print("Verify token:", verify_token("alice", token))

# --- Authorization ---

def is_admin(user_role):
    return user_role == "admin"

print("Is admin:", is_admin("admin"))
print("Is admin:", is_admin("user"))

# --- CORS Headers ---

def add_cors_headers(response_headers):
    response_headers["Access-Control-Allow-Origin"] = "*"
    response_headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE"
    return response_headers

headers = {}
headers = add_cors_headers(headers)
print("Response headers with CORS:", headers)

# --- Exercises ---

# Exercise 1:
# Improve password hashing with salt and pepper.

# Exercise 2:
# Implement role-based access control for routes.

# Exercise 3:
# Add CSRF protection to POST requests.
