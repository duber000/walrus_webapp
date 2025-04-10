# Chapter 17: Templates and Static Files

# This chapter introduces HTML templating and serving static files.

from jinja2 import Template

# --- HTML Templates with Jinja2 ---

template_str = """
<html>
<head><title>{{ title }}</title></head>
<body>
<h1>{{ heading }}</h1>
<ul>
{% for item in items %}
<li>{{ item }}</li>
{% endfor %}
</ul>
</body>
</html>
"""

template = Template(template_str)
html = template.render(title="My Page", heading="Welcome!", items=["Apple", "Banana", "Cherry"])
print(html)

# --- Serving Static Files (concept) ---

def serve_static_file(path):
    try:
        with open(f"static/{path}", "r") as f:
            return f.read()
    except FileNotFoundError:
        return "404 Not Found"

# Example usage:
# print(serve_static_file("style.css"))

# --- Exercises ---

# Exercise 1:
# Create an HTML template for a user profile page.

# Exercise 2:
# Add template inheritance (base.html + child templates).

# Exercise 3:
# Serve CSS and JS files from a static directory.
