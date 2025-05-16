#5
# Operation: Get the weekday name from a date

import calendar
from datetime import datetime

d = datetime.strptime("2025-05-07", "%Y-%m-%d")
day_name = calendar.day_name[d.weekday()]
print("Day name:", day_name)
# Output: Day name: Wednesday
