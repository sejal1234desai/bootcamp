#5# Operation: Write a simple function that returns system status for debugging

import os

def health_check():
    status = "OK" if os.system("ping -c 1 google.com") == 0 else "DOWN"
    return {"status": status, "system_load": os.getloadavg()}

# Example usage:
print(health_check())

# Output:
# {'status': 'OK', 'system_load': (0.78, 0.62, 0.58)}
