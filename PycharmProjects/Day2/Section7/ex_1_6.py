## Operation: Compare built-in sorted() with a custom sorting function

import random
import time

# Custom sort function (Bubble Sort)
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Generate random list
random_list = random.sample(range(10000), 1000)

# Benchmark built-in sorted()
start = time.time()
sorted_list = sorted(random_list)
builtin_sort_time = time.time() - start

# Benchmark custom sort
start = time.time()
bubble_sort(random_list)
custom_sort_time = time.time() - start

print(f"Built-in sort time: {builtin_sort_time:.6f} seconds")
print(f"Custom sort time: {custom_sort_time:.6f} seconds")

# Output:
# Built-in sort should be much faster than the bubble sort due to its optimized algorithm.
