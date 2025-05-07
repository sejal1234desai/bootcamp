#5
# Operation: Formatting Log Output

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logger.debug("This is a debug message with a timestamp.")
# Output: 2025-05-07 12:00:00,001 - DEBUG - This is a debug message with a timestamp.
