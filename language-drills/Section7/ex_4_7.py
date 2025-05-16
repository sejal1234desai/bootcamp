#7
# Operation: Print current memory and CPU info using psutil or os.getloadavg()

import psutil

def print_resource_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage}%")

# Example usage:
print_resource_usage()

# Output (example):
# CPU Usage: 15.2%
# Memory Usage: 72.5%
