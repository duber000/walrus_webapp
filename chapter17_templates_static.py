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

# --- Save user exercises to webapp/routes.py ---

def save_exercises_to_webapp():
    exercises_code = "\n# --- Chapter 17 User Exercises ---\n"

    # Exercise 1: /profile-template
    exercises_code += (
        "from jinja2 import Template\n"
        "def profile_template_route():\n"
        "    template_str = '''<html><body><h1>User: {{ username }}</h1><p>Email: {{ email }}</p></body></html>'''\n"
        "    template = Template(template_str)\n"
        "    return template.render(username='alice', email='alice@example.com')\n"
        "routes['/profile-template'] = profile_template_route\n\n"
    )

    # Exercise 2: /base-child-template
    exercises_code += (
        "def base_child_template_route():\n"
        "    base = '''<html><body>{% block content %}{% endblock %}</body></html>'''\n"
        "    child = '''{% extends base %}{% block content %}<h2>Child Content</h2>{% endblock %}'''\n"
        "    from jinja2 import Environment, DictLoader\n"
        "    env = Environment(loader=DictLoader({'base': base, 'child': child}))\n"
        "    template = env.get_template('child')\n"
        "    return template.render()\n"
        "routes['/base-child-template'] = base_child_template_route\n\n"
    )

    # Exercise 3: /static-file
    exercises_code += (
        "def static_file_route(filename='style.css'):\n"
        "    try:\n"
        "        with open(f'static/{filename}', 'r') as f:\n"
        "            return f.read()\n"
        "    except FileNotFoundError:\n"
        "        return '404 Not Found'\n"
        "routes['/static-file'] = static_file_route\n\n"
    )

    # Append or update the exercises in webapp/routes.py
    with open('webapp/routes.py', 'r') as f:
        content = f.read()

    marker = '# --- Chapter 17 User Exercises ---'
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

    print("Saved your Chapter 17 exercises to webapp/routes.py!")

if __name__ == "__main__":
    save_exercises_to_webapp()
