# Chapter 9: Object-Oriented Programming

# This chapter introduces classes, objects, methods, and inheritance.

# --- Data Classes (Python 3.7+) ---

from dataclasses import dataclass

@dataclass
class User:
    username: str
    email: str
    is_active: bool = True

u = User("alice", "alice@example.com")
print(u)

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
        handler = self.routes.get(request.url)
        if handler:
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
