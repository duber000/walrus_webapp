# webapp/utils.py
# Utility functions

def safe_json_loads(data, default=None):
    """
    Safely parse JSON data, returning a default value on error.
    """
    import json
    try:
        return json.loads(data)
    except Exception:
        return default

def safe_int(val, default=0):
    try:
        return int(val)
    except Exception:
        return default
