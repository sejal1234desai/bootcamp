#8# Operation: Raise the actual error after logging it

import logging

# Setup logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

def risky_operation():
    try:
        # Simulate an error
        result = 1 / 0
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise e  # Re-raise the original error after logging

# Example usage:
risky_operation()

# Output:
# ERROR:__main__:An error occurred: division by zero
# The exception is raised after logging, allowing for debugging before termination.
