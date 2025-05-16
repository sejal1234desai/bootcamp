# Operation: Start a long process and kill it after delay

import subprocess, time

proc = subprocess.Popen(["sleep", "10"])
print("Started process, PID:", proc.pid)
time.sleep(2)
proc.terminate()
print("Process killed")
# Output:
# Started process, PID: 12345
# Process killed
