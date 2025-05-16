# Operation: Use ThreadPoolExecutor to parallelize

from concurrent.futures import ThreadPoolExecutor

def double(x):
    return x * 2

with ThreadPoolExecutor() as executor:
    results = list(executor.map(double, range(5)))

print("Doubled:", results)
# Output: Doubled: [0, 2, 4, 6, 8]
