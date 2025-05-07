#3
# Operation: Adding Contextual Information in Logs

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

user = {"name": "Sejal", "age": 22}

# Log contextual information
logger.debug(f"User: {user['name']}, Age: {user['age']}")
# Output: 2025-05-07 12:00:00,001 - DEBUG - User: Sejal, Age: 22
