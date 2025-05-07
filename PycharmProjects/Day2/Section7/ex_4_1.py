#
# Operation: Log user ID and function name in each message

import logging

# Setup logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def log_user_activity(user_id, activity):
    logger.info(f"User ID: {user_id} - Activity: {activity} - Function: {log_user_activity.__name__}")

# Example usage:
log_user_activity(123, "Login")

# Output:
# INFO:__main__:User ID: 123 - Activity: Login - Function: log_user_activity
