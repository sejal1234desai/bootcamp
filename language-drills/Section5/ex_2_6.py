## Operation: Copy a file using shutil

import shutil
from pathlib import Path

# Prepare source file
src = Path("source.txt")
src.write_text("copy me")

dst = Path("destination.txt")
shutil.copy(src, dst)

print(dst.read_text())
# Output: copy me

