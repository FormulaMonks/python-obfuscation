from functools import wraps

from flask import render_template


def render_to(tpl):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            out = func(*args, **kwargs) or {}
            if isinstance(out, dict):
                out = render_template(tpl, **out)
            return out
        return wrapper
    return decorator
