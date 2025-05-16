#2# Operation: Compare memory usage between a generator and a list

import sys

# Create a list and a generator
my_list = [x * x for x in range(1000000)]
my_generator = (x * x for x in range(1000000))

# Compare memory usage
list_size = sys.getsizeof(my_list)
generator_size = sys.getsizeof(my_generator)

print(f"List memory usage: {list_size} bytes")
print(f"Generator memory usage: {generator_size} bytes")

# Output:
# The generator will use significantly less memory than the list, as it generates values lazily.
