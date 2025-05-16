# Operation: Use Prefix for Boolean Function Names

# Bad practice: ambiguous function name
def check_user_active(user):
    return user.active

# Improved with clear boolean function naming
def is_user_active(user):
    return user.active

# Output:
# The function name `is_user_active()` is clear and indicates that the return value is a boolean.
