#
# Operation: Find most common elements in a list

from collections import Counter

nums = [1, 2, 3, 2, 4, 2, 3, 1, 1, 5]
count = Counter(nums)

print(count.most_common(2))
# Output: [(2, 3), (1, 3)]
