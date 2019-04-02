import inspect
from . import jinja_functions


def collect_jinja2_functions():
    """
    Collects jinja2 functions
    """
    jinja_functions_settings = {}
    funcs = inspect.getmembers(jinja_functions, inspect.isfunction)

    for f in funcs:
        name = f[0]
        callable_func = f[1]
        if name.startswith('_'):
            continue

        jinja_functions_settings[name] = callable_func

    return jinja_functions_settings
