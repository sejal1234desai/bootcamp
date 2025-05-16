#7
# Operation: Using __name__ as Logger Name

import logging

# Logger with module name
logger = logging.getLogger(__name__)

logger.info("This log message comes from a specific module.")
# Output: 2025-05-07 12:00:00,001 - INFO - This log message comes from a specific module.
