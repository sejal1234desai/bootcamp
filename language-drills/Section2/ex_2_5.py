#5. map_filter_example

nums = [1, 2, 3, 4]

doubled = list(map(lambda x: x * 2, nums))
filtered = list(filter(lambda x: x % 2 != 0, nums))

print(doubled)  # Output: [2, 4, 6, 8]
print(filtered) # Output: [1, 3]
