## Operation: Use line_profiler for per-line profiling

# Install line_profiler via pip:
# pip install line_profiler

# Decorate function with @profile to measure per-line timing
@profile
def example_function():
    sum(range(1000000))

if __name__ == '__main__':
    example_function()

# Output:
# After running with kernprof -l yourscript.py, you can view line-by-line performance by running:
# kernprof -v yourscript.py.lprof
