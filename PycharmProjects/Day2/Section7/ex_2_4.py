#4
# Operation: Use any() to short-circuit checking if a number in a list is divisible by 99

numbers = [x for x in range(1000000)]

# Check if any number is divisible by 99
result = any(x % 99 == 0 for x in numbers)
print(f"Any number divisible by 99: {result}")

# Output:
# Short-circuiting will stop as soon as it finds a number divisible by 99, improving efficiency.
