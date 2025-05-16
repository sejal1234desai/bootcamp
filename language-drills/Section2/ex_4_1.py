#1. basic_file_context

with open("sample.txt", "w") as f:
    f.write("Hello, Context Manager!")

with open("sample.txt", "r") as f:
    content = f.read()
    print("File content:", content)

# Output:
# File content: Hello, Context Manager!
