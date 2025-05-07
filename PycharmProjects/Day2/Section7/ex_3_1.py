#1
# Operation: Pause execution using pdb.set_trace() and inspect local variables

import pdb

def calculate_sum(a, b):
    pdb.set_trace()  # Pauses execution here
    result = a + b
    return result

# Example usage:
calculate_sum(3, 4)

# Output:
# The program will pause at pdb.set_trace() and allow you to inspect the variables 'a', 'b', and 'result' in the debugger.
# Use commands like 'p a', 'p b', and 'p result' to inspect the variables.
