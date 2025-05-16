#5# Operation: Use itertools.islice to read the first N lines from a generator

import itertools

def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line

# Get the first 10 lines without loading the entire file
first_10_lines = itertools.islice(read_large_file('large_file.txt'), 10)

for line in first_10_lines:
    print(line.strip())

# Output:
# Only the first 10 lines of the file will be processed, avoiding loading the rest of the file.

