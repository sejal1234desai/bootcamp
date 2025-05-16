#custom_exception

class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")

try:
    check_age(-5)
except InvalidAgeError as e:
    print("Error:", e)

# Output:
# Error: Age cannot be negative
