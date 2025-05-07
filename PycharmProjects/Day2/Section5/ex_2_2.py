#2
# Operation: List all Python files in current directory

from pathlib import Path

py_files = list(Path(".").glob("*.py"))
for file in py_files:
    print(file.name)
# Output: list of .py files like "read_file_pathlib.py", etc.
