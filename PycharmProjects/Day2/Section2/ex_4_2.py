#2. multiple_contexts

with open("file1.txt", "w") as f1, open("file2.txt", "w") as f2:
    f1.write("File 1 content")
    f2.write("File 2 content")

# Output:
# (Creates and writes to file1.txt and file2.txt)
