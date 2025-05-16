## Operation: Measure Memory Usage with memory_profiler

# Install memory_profiler via pip:
# pip install memory_profiler

from memory_profiler import profile

@profile
def example_function():
    data = [x * x for x in range(1000000)]
    return data

if __name__ == '__main__':
    example_function()

# Output:
# After running with `python -m memory_profiler yourscript.py`, you can see memory usage before and after the function call.
