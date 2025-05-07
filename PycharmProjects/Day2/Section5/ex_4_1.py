#
# Operation: Serialize and deserialize a Python dict using JSON

import json

data = {"name": "Sejal", "role": "developer"}
json_str = json.dumps(data)
print("Serialized JSON:", json_str)

original = json.loads(json_str)
print("Deserialized dict:", original)
# Output:
# Serialized JSON: {"name": "Sejal", "role": "developer"}
# Deserialized dict: {'name': 'Sejal', 'role': 'developer'}
