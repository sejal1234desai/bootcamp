#7
# Operation: Serialize datetime object using a custom encoder

import json
from datetime import datetime

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

data = {"event": "login", "time": datetime.now()}
encoded = json.dumps(data, cls=DateTimeEncoder)
print("JSON with datetime:", encoded)
