# Operation: Enable debug logs only when DEBUG=True

import logging
import os

# Setup logger
logger = logging.getLogger(__name__)

# Check for environment variable to enable debug mode
DEBUG = os.getenv('DEBUG', 'False') == 'True'
logging.basicConfig(level=logging.DEBUG if DEBUG else logging.INFO)

def debug_function():
    logger.debug("This is a debug log.")
    logger.info("This is an info log.")

# Example usage:
debug_function()

# Set DEBUG=True in your environment variables to see the debug log.
