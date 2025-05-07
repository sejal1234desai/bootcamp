#8
# Operation: Check if file exists and is a file

from pathlib import Path

path = Path("check_file_exists.txt")
path.write_text("exists")

print(path.exists())    # Output: True
print(path.is_file())   # Output: True

# Clean up
path.unlink()

