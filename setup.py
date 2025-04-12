from setuptools import setup, find_packages
import os

def create_webapp_structure():
    os.makedirs("webapp", exist_ok=True)
    open("webapp/__init__.py", "a").close()

    modules = ["routes.py", "server.py", "models.py", "utils.py"]
    for module in modules:
        path = os.path.join("webapp", module)
        if not os.path.exists(path):
            with open(path, "w") as f:
                if module == "routes.py":
                    f.write(
                        "# webapp/routes.py\n"
                        "routes = {\n"
                        "    '/': 'home page',\n"
                        "    '/about': 'about page'\n"
                        "}\n"
                        "\n"
                        "def get_route(url):\n"
                        "    return routes.get(url, '404 Not Found')\n"
                    )
                elif module == "server.py":
                    f.write(
                        "# webapp/server.py\n"
                        "def start_server():\n"
                        "    print('Starting server...')\n"
                    )
                elif module == "models.py":
                    f.write(
                        "# webapp/models.py\n"
                        "# Define your data models here (e.g., User, Post)\n"
                    )
                elif module == "utils.py":
                    f.write(
                        "# webapp/utils.py\n"
                        "# Utility functions\n"
                        "def safe_json_loads(data, default=None):\n"
                        "    import json\n"
                        "    try:\n"
                        "        return json.loads(data)\n"
                        "    except Exception:\n"
                        "        return default\n"
                        "\n"
                        "def safe_int(val, default=0):\n"
                        "    try:\n"
                        "        return int(val)\n"
                        "    except Exception:\n"
                        "        return default\n"
                    )

create_webapp_structure()

setup(
    name="python-learning-webapp",
    version="0.1",
    packages=find_packages(),
    description="Incremental Python learning project culminating in a web framework",
    author="Your Name",
    author_email="your@email.com",
    install_requires=[
        "tortoise-orm>=0.20.0"
    ],
    python_requires=">=3.7",
)
