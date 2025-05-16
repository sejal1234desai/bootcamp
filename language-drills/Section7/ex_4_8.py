#8
# Operation: Wrap functions with decorators to log their name, args, and return value

import logging

# Setup logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def trace_function_calls(func):
    def wrapper(*args, **kwargs):
        logger.info(f"Function {func.__name__} called with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

@trace_function_calls
def add(a, b):
    return a + b

# Example usage:
add(2, 3)

# Output:
# INFO:__main__:Function add called with args=(2, 3), kwargs={}
# INFO:__main__:Function add returned 5
