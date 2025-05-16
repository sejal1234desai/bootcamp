#4
# Operation: Replacing print statements with logging

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Replacing print with logger
user = {"name": "Sejal", "age": 22}
logger.info(f"User Information: {user}")
# Output: 2025-05-07 12:00:00,001 - INFO - User Information: {'name': 'Sejal', 'age': 22}
