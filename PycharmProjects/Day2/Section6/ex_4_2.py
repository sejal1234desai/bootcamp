#
# Operation: Using Logging Levels

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")

# Output:
# 2025-05-07 12:00:00,001 - DEBUG - This is a debug message.
# 2025-05-07 12:00:01,001 - INFO - This is an info message.
# 2025-05-07 12:00:02,001 - WARNING - This is a warning message.
# 2025-05-07 12:00:03,001 - ERROR - This is an error message.
# 2025-05-07 12:00:04,001 - CRITICAL - This is a critical message.
