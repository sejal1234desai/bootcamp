## Operation: Read large file line by line using a generator

def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line

# Example usage
for line in read_large_file('large_file.txt'):
    print(line.strip())  # Process each line lazily

# Output:
# Each line will be processed as it is read from the file, which avoids loading the entire file into memory.
