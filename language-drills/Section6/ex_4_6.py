#6
# Operation: Logging to a File

import logging

logging.basicConfig(filename="app.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logger.info("This is a log message to a file.")
# The log message will be saved to 'app.log' instead of being printed to stdout.
