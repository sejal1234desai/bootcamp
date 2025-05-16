#3
# Operation: Write to a file using pathlib

from pathlib import Path

path = Path("output.txt")
path.write_text("hello")

print(path.read_text())
# Output: hello
