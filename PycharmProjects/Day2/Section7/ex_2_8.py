#8
# Operation: Use yield to replace a list append operation

# Using list append
def collect_squares_list(n):
    result = []
    for x in range(n):
        result.append(x * x)
    return result

# Using yield (generator version)
def collect_squares_generator(n):
    for x in range(n):
        yield x * x

# Example usage:
squares_list = collect_squares_list(1000)
squares_gen = collect_squares_generator(1000)

print(f"List length: {len(squares_list)}")
print(f"Generator length: Not available (generator is lazy)")

# Output:
# The generator uses less memory than the list as it yields one value at a time.
