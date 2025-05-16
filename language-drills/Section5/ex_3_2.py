#
# Operation: Add 7 days to today

from datetime import datetime, timedelta

today = datetime.now()
future = today + timedelta(days=7)
print("Today:", today.date())
print("7 days later:", future.date())
# Output: 7 days later: YYYY-MM-DD (7 days ahead)
