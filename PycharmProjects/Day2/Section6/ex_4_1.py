#
# Operation: Setting up a Logger

import logging

# Setting up basic configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Log a message
logger.info("Logger initialized successfully.")
# Output: 2025-05-07 12:00:00,000 - INFO - Logger initialized successfully.
