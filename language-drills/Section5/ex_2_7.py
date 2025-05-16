#7
# Operation: Show absolute and relative paths

from pathlib import Path

rel = Path("myfile.txt")
abs_path = rel.resolve()

print("Relative:", rel)
print("Absolute:", abs_path)
# Output: Relative: myfile.txt
#         Absolute: /full/path/to/myfile.txt
