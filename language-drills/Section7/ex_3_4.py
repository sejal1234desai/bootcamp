#4.
# Operation: Log function entry and exit using logger.debug()

import logging

# Setup logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

def example_function(a, b):
    logger.debug(f"Entering example_function with a={a}, b={b}")
    result = a + b
    logger.debug(f"Exiting example_function with result={result}")
    return result

# Example usage:
example_function(5, 3)

# Output:
# DEBUG:__main__:Entering example_function with a=5, b=3
# DEBUG:__main__:Exiting example_function with result=8
