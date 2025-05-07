## Operation: Time execution with timeit

import timeit

# Timing sum(range(10000)) using timeit
execution_time = timeit.timeit('sum(range(10000))', number=1000)
print(f"Execution time: {execution_time:.6f} seconds")

# Output:
# Execution time: (The result will vary, but it will be the time taken to execute the sum operation 1000 times.)
