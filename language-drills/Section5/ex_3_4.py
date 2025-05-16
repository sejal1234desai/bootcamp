#4.
# Operation: Parse date string to datetime object

from datetime import datetime

date_str = "2024-01-01"
parsed = datetime.strptime(date_str, "%Y-%m-%d")
print("Parsed:", parsed)
# Output: Parsed: 2024-01-01 00:00:00
