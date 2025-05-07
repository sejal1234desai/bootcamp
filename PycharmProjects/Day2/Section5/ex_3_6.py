#6
# Operation: Compare two dates

from datetime import datetime

date1 = datetime(2024, 5, 1)
date2 = datetime(2025, 1, 1)

if date1 < date2:
    print("Date1 is earlier")
else:
    print("Date2 is earlier")
# Output: Date1 is earlier
