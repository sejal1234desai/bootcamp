#8
# Operation: Round datetime to top of the hour

from datetime import datetime, timedelta

now = datetime.now()
rounded = now.replace(minute=0, second=0, microsecond=0)
if now.minute >= 30:
    rounded += timedelta(hours=1)

print("Original:", now)
print("Rounded:", rounded)
# Output:
# Original: 2025-05-07 14:47:23.345123
# Rounded: 2025-05-07 15:00:00
