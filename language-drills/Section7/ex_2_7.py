#7
# Operation: Copy a file line by line without loading it entirely into memory

def copy_file_line_by_line(source_file, destination_file):
    with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
        for line in src:
            dest.write(line)

# Example usage:
copy_file_line_by_line('source.txt', 'destination.txt')

# Output:
# The file is copied line by line, ensuring that large files don't consume too much memory.
