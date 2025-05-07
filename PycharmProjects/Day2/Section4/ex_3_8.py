#8
# Operation: Decorator with @wraps that logs before/after function execution

from functools import wraps

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Starting {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Ending {func.__name__}")
        return result
    return wrapper

@log_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Sejal")
# Output:
# Starting greet
# Hello, Sejal!
# Ending greet
