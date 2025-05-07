#8
# Operation: Generate permutations and combinations

from itertools import permutations, combinations

data = [1, 2, 3]

print("Permutations of 2:", list(permutations(data, 2)))
# Output: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

print("Combinations of 2:", list(combinations(data, 2)))
# Output: [(1, 2), (1, 3), (2, 3)]

print("Combinations of 3:", list(combinations(data, 3)))
# Output: [(1, 2, 3)]
