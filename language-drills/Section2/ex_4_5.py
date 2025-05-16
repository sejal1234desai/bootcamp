#5. suppressing_exceptions

from contextlib import suppress

with suppress(FileNotFoundError):
    with open("nonexistent.txt") as f:
        data = f.read()

print("Continued even though file not found")

# Output:
# Continued even though file not found
