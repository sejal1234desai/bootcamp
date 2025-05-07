## Operation: Manually Time Execution with time

import time

start_time = time.time()

# Example function to time
sum(range(1000000))

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.6f} seconds")

# Output:
# This will manually measure the time taken to run the sum operation.
