## Operation: Read file using pathlib

from pathlib import Path

# Make sure file exists first
Path("myfile.txt").write_text("Test content")

content = Path("myfile.txt").read_text()
print(content)
# Output: Test content
