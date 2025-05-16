#
# Operation: Avoid temporary lists by using a generator expression

# Sum the squares of numbers without creating an intermediate list
result = sum(x * x for x in range(1000000))
print(f"Sum of squares: {result}")

# Output:
# The generator expression avoids creating a list, saving memory and improving efficiency.
