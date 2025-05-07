# Operation: Use @wraps to preserve function metadata in decorator

from functools import wraps

def log_info(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling function...")
        return func(*args, **kwargs)
    return wrapper

@log_info
def hello():
    """This function says hello"""
    print("Hello!")

hello()
print(hello.__name__)      # Output: hello
print(hello.__doc__)       # Output: This function says hello
