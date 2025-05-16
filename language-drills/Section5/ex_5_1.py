# Operation: Run a shell command using subprocess
# Linux/Mac: ["ls", "-l"] | Windows: ["cmd", "/c", "dir"]

import subprocess

result = subprocess.run(["ls", "-l"])

