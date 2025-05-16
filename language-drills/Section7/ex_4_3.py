#3# Operation: Include error codes in log messages for easier tracing

import logging

# Setup logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def perform_action():
    try:
        # Simulate an error
        result = 1 / 0
    except Exception as e:
        logger.error(f"Error ID: 12345 - Message: {e}")

# Example usage:
perform_action()

# Output:
# ERROR:__main__:Error ID: 12345 - Message: division by zero
