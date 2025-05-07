#
# Operation: Format today's date as YYYY-MM-DD

from datetime import datetime

today = datetime.now()
formatted = today.strftime("%Y-%m-%d")
print("Formatted date:", formatted)
# Output: Formatted date: 2025-05-07 (or whatever today's date is)
