# Operation: partial() to fix base to 2 in int conversion

from functools import partial

# Fix base=2 for int function using partial
binary_to_int = partial(int, base=2)

print(binary_to_int('1010'))  # Output: 10
