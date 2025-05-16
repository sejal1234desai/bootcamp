# Operation: Check if subprocess failed

import subprocess

res = subprocess.run(["false"])  # 'false' returns exit code 1
if res.returncode != 0:
    print("Command failed with code:", res.returncode)
# Output: Command failed with code: 1
