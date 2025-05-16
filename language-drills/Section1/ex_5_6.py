#reraise_exception
try:
    raise ValueError("Something went wrong")
except ValueError as e:
    print("Logging error:", e)
    raise

# Output:
# Logging error: Something went wrong
# Traceback (most recent call last):

# ValueError: Something went wrong
