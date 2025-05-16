#
# Operation: Compare List vs Generator Performance

import time

# List comprehension
start = time.time()
list_comprehension = [x*x for x in range(1000000)]
list_time = time.time() - start

# Generator expression
start = time.time()
generator_expression = (x*x for x in range(1000000))
generator_time = time.time() - start

print(f"List comprehension time: {list_time:.6f} seconds")
print(f"Generator expression time: {generator_time:.6f} seconds")

# Output:
# The list comprehension is expected to take more time and memory since it constructs the entire list in memory.
# The generator expression is more memory-efficient as it lazily generates values.
