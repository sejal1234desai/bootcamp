#5
# Operation: Use islice to skip and take from a range

from itertools import islice

result = list(islice(range(10), 3, 7))  # skip first 3, take next 4

print(result)  # Output: [3, 4, 5, 6]
