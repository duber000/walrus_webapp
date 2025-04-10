# webapp/routes.py
routes = {
    '/': 'home page',
    '/about': 'about page'
}

def get_route(url):
    return routes.get(url, '404 Not Found')
