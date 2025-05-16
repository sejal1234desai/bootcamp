#multiple_exceptions

try:
    x = int("abc")  # Change to: x = 10 / 0 to test ZeroDivisionError
except ValueError:
    print("Invalid value!")
except ZeroDivisionError:
    print("Cannot divide by zero")

# Output (as-is):
# Invalid value!
