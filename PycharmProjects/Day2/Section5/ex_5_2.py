# Operation: Capture command output using capture_output=True

import subprocess

res = subprocess.run(["echo", "Hello Sejal"], capture_output=True, text=True)
print("Captured Output:", res.stdout.strip())
# Output: Captured Output: Hello Sejal
