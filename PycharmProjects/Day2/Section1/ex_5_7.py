#suppress_exception

from contextlib import suppress

d = {"name": "Alice"}

with suppress(KeyError):
    print(d["age"])

print("No crash!")

# Output:
# No crash!
