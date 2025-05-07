#6
# Operation: Explain pickle danger and show JSON as safer alternative

import pickle, json

# DANGER: Pickle can execute arbitrary code (avoid untrusted input)
# Safe alternative → use json for basic types

malicious = b"cos\nsystem\n(S'echo HACKED'\ntR."
# DON'T RUN THIS: pickle.loads(malicious)

safe_data = {"x": 1, "y": 2}
json_safe = json.dumps(safe_data)
print("Safe JSON:", json_safe)
