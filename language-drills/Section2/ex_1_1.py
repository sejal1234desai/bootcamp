#1. eafp_basics

person = {"name": "Alice"}

try:
    print(person["age"])  # KeyError
except KeyError:
    print("Key 'age' not found.")

# Output:
# Key 'age' not found.
