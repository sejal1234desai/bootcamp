#
# Operation: Add timing to log output to trace slow functions

import logging
import time

# Setup logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def track_performance(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        logger.info(f"Function {func.__name__} executed in {duration:.4f} seconds")
        return result
    return wrapper

@track_performance
def slow_function():
    time.sleep(2)

# Example usage:
slow_function()

# Output:
# INFO:__main__:Function slow_function executed in 2.0001 seconds
