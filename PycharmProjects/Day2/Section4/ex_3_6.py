# Operation: Use reduce to calculate factorial

from functools import reduce

n = 5
factorial = reduce(lambda x, y: x * y, range(1, n+1))

print(factorial)  # Output: 120
