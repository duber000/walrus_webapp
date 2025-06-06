# Chapter 9: Object-Oriented Programming

# This chapter introduces classes, objects, methods, inheritance,
# and some modern Python features like dataclasses and immutability.

# --- Data Classes (Python 3.7+) ---

# A dataclass is a Python class designed mainly to store data.
# It automatically generates __init__, __repr__, __eq__, and other methods,
# so you don't have to write boilerplate code.
# You just declare the fields, and Python handles the rest.

from dataclasses import dataclass, replace as dc_replace
import copy

@dataclass
class User:
    username: str
    email: str
    is_active: bool = True

u = User("alice", "alice@example.com")
print(u)

# --- Immutable Data Classes (frozen=True) ---

# By default, dataclass instances are mutable: you can change their fields.
# If you want to make them immutable (read-only), set frozen=True.
# This is useful for data you don't want to accidentally modify,
# similar to tuples or namedtuples.

@dataclass(frozen=True)
class UserProfile:
    username: str
    email: str
    python_version: str

profile = UserProfile("alice", "alice@example.com", "3.12")
print("Original profile:", profile)

# Since frozen dataclasses are immutable, you can't do:
# profile.python_version = "3.13"  # This would raise FrozenInstanceError

# Instead, to "modify" an immutable dataclass, you create a *new* instance
# with the updated values. The dataclasses.replace() function helps with this.

# Before Python 3.13, use dataclasses.replace()
updated_profile = dc_replace(profile, python_version="3.13")
print("Updated profile (old way):", updated_profile)

# From Python 3.13, you can use copy.replace()
updated_profile2 = copy.replace(profile, python_version="3.13")
print("Updated profile (new way):", updated_profile2)

# --- Basic class ---

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name}."

p = Person("Alice", 30)
print(p.greet())

# --- Inheritance ---

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):
        return f"Hi, I'm {self.name} and my student ID is {self.student_id}."

s = Student("Bob", 20, "S12345")
print(s.greet())

# --- Mini Web Framework: OOP Design ---

class Request:
    def __init__(self, url):
        self.url = url

class Response:
    def __init__(self, content, status=200):
        self.content = content
        self.status = status

    def __str__(self):
        return f"{self.status} OK: {self.content}" if self.status == 200 else f"{self.status} Error: {self.content}"

class App:
    def __init__(self):
        self.routes = {}

    def add_route(self, url, handler):
        self.routes[url] = handler

    def handle_request(self, request):
        if (handler := self.routes.get(request.url)):
            return Response(handler())
        else:
            return Response("Not Found", status=404)

app = App()
app.add_route("/", lambda: "home page")
app.add_route("/about", lambda: "about page")

req = Request("/about")
res = app.handle_request(req)
print(res)

req2 = Request("/missing")
res2 = app.handle_request(req2)
print(res2)

# --- Exercises ---

# Exercise 1:
# Create a class `Car` with attributes make, model, year, and a method to display info.

# Exercise 2:
# Extend the mini web framework with a `Router` class that supports dynamic routes.

# Exercise 3:
# Add a `User` class with login/logout methods.

# --- Python 3.13+: TypeVar defaults for generics (PEP 696) ---

from typing import TypeVar, Generic

T = TypeVar("T", default=int)
U = TypeVar("U", default=str)

class Pair(Generic[T, U]):
    def __init__(self, first: T, second: U):
        self.first = first
        self.second = second

    def __repr__(self):
        return f"Pair({self.first!r}, {self.second!r})"

p_default = Pair(1, "hello")  # uses defaults int, str
print("Default Pair:", p_default)

p_partial = Pair[float](3.14, "pi")  # overrides T, keeps U default
print("Partial override Pair:", p_partial)

p_full = Pair[float, bytes](2.71, b"e")  # overrides both
print("Full override Pair:", p_full)

# --- Python 3.13+: TypeIs for type narrowing (PEP 742) ---

from typing import TypeIs

def is_positive_int(x: int | float) -> TypeIs[int]:
    """Return True if x is a positive int (not float)."""
    return isinstance(x, int) and x > 0

def process_number(x: int | float):
    if is_positive_int(x):
        # Type checker now knows x is int here
        print(f"Positive integer: {x} (squared: {x * x})")
    else:
        # x is still int | float here
        print(f"Not a positive integer: {x}")

process_number(5)
process_number(-3)
process_number(3.14)

# --- Save user exercises to webapp/routes.py ---

def save_exercises_to_webapp():
    exercises_code = "\n# --- Chapter 9 User Exercises ---\n"

    # Exercise 1: /car-info
    exercises_code += (
        "class Car:\n"
        "    def __init__(self, make, model, year):\n"
        "        self.make = make\n"
        "        self.model = model\n"
        "        self.year = year\n"
        "    def display_info(self):\n"
        "        return f'{self.year} {self.make} {self.model}'\n"
        "def car_info_route():\n"
        "    car = Car('Toyota', 'Corolla', 2020)\n"
        "    return car.display_info()\n"
        "routes['/car-info'] = car_info_route\n\n"
    )

    # Exercise 2: /dynamic-route/<name>
    exercises_code += (
        "class Router:\n"
        "    def __init__(self):\n"
        "        self.routes = {}\n"
        "    def add_route(self, pattern, handler):\n"
        "        self.routes[pattern] = handler\n"
        "    def handle(self, path):\n"
        "        import re\n"
        "        for pattern, handler in self.routes.items():\n"
        "            match = re.match(pattern, path)\n"
        "            if match:\n"
        "                return handler(**match.groupdict())\n"
        "        return '404 Not Found'\n"
        "router = Router()\n"
        "def dynamic_route(name):\n"
        "    return f'Hello, {name}!'\n"
        "router.add_route(r'^/dynamic-route/(?P<name>\\w+)$', dynamic_route)\n"
        "def dynamic_route_route(name):\n"
        "    return router.handle(f'/dynamic-route/{name}')\n"
        "routes['/dynamic-route/<name>'] = dynamic_route_route\n\n"
    )

    # Exercise 3: /user-login
    exercises_code += (
        "class User:\n"
        "    def __init__(self, username):\n"
        "        self.username = username\n"
        "        self.logged_in = False\n"
        "    def login(self):\n"
        "        self.logged_in = True\n"
        "        return f'{self.username} logged in.'\n"
        "    def logout(self):\n"
        "        self.logged_in = False\n"
        "        return f'{self.username} logged out.'\n"
        "def user_login_route():\n"
        "    user = User('alice')\n"
        "    login_msg = user.login()\n"
        "    logout_msg = user.logout()\n"
        "    return login_msg + ' ' + logout_msg\n"
        "routes['/user-login'] = user_login_route\n\n"
    )

    # Append or update the exercises in webapp/routes.py
    with open("webapp/routes.py", "r") as f:
        content = f.read()

    marker = "# --- Chapter 9 User Exercises ---"
    if marker in content:
        pre = content.split(marker)[0]
        post = content.split(marker)[-1]
        post_lines = post.splitlines()
        idx = 0
        for i, line in enumerate(post_lines):
            if line.strip().startswith("# ---"):
                idx = i
                break
        else:
            idx = len(post_lines)
        post = "\n".join(post_lines[idx:])
        new_content = pre + exercises_code + post
    else:
        new_content = content + "\n" + exercises_code

    with open("webapp/routes.py", "w") as f:
        f.write(new_content)

    print("Saved your Chapter 9 exercises to webapp/routes.py!")

if __name__ == "__main__":
    save_exercises_to_webapp()
