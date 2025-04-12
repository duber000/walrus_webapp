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

# --- Save user exercises to webapp/routes.py ---

def save_exercises_to_webapp():
    exercises_code = "\n# --- Chapter 16 User Exercises ---\n"

    # Exercise 1: improved password hashing
    exercises_code += (
        "import hashlib\n"
        "def hash_password_pepper(password, salt='somesalt', pepper='superpepper'):\n"
        "    return hashlib.sha256((salt + password + pepper).encode()).hexdigest()\n\n"
    )

    # Exercise 2: role-based access control
    exercises_code += (
        "def role_required(role):\n"
        "    def decorator(func):\n"
        "        def wrapper(*args, **kwargs):\n"
        "            user_role = kwargs.get('user_role', 'user')\n"
        "            if user_role == role:\n"
        "                return func(*args, **kwargs)\n"
        "            else:\n"
        "                return '403 Forbidden: Insufficient role'\n"
        "        return wrapper\n"
        "    return decorator\n\n"
        "@role_required('admin')\n"
        "def admin_only_route(user_role='user'):\n"
        "    return 'Welcome, admin!'\n"
        "routes['/admin-only'] = admin_only_route\n\n"
    )

    # Exercise 3: CSRF protection
    exercises_code += (
        "def csrf_protect_route(request):\n"
        "    token = request.headers.get('X-CSRF-Token')\n"
        "    if token == 'known_token':\n"
        "        return 'CSRF check passed.'\n"
        "    else:\n"
        "        return '403 Forbidden: CSRF token missing or invalid.'\n"
        "routes['/csrf-protect'] = csrf_protect_route\n\n"
    )

    # Append or update the exercises in webapp/routes.py
    with open('webapp/routes.py', 'r') as f:
        content = f.read()

    marker = '# --- Chapter 16 User Exercises ---'
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

    print("Saved your Chapter 16 exercises to webapp/routes.py!")

if __name__ == "__main__":
    save_exercises_to_webapp()
