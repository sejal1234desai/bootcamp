#7. safe_type_conversion

user_input = "abc"

try:
    val = int(user_input)
    print("Converted:", val)
except ValueError:
    print("Invalid input; not a number.")

# Output:
# Invalid input; not a number.
