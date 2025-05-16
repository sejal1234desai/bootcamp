# Operation: Replace Magic Values with Named Constants

# Bad Practice: Magic values
def retry_request():
    for _ in range(3):
        # some logic
        pass

# Improved with named constants
MAX_RETRIES = 3

def retry_request():
    for _ in range(MAX_RETRIES):
        # some logic
        pass

# Output:
# The constant MAX_RETRIES makes the code more readable and easier to maintain.
