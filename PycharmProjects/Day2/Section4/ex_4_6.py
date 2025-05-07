#6
# Operation: Duplicate an iterator using tee()

from itertools import tee

data = iter([10, 20, 30, 40])
a, b = tee(data)

print(list(a))  # Output: [10, 20, 30, 40]
print(list(b))  # Output: [10, 20, 30, 40]
