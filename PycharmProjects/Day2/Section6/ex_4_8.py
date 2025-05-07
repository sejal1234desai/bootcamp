#8
# Operation: Conditional Logging Based on Debug Flag

import logging

DEBUG = True  # Set this flag to control debug-level logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

if DEBUG:
    logger.debug("This is a debug message.")
    # Output: 2025-05-07 12:00:00,001 - DEBUG - This is a debug message.
