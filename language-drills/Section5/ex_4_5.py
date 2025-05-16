#5
# Operation: Serialize and deserialize a Python object with pickle

import pickle

data = {"topic": "serialization", "type": "pickle"}
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

with open("data.pkl", "rb") as f:
    loaded = pickle.load(f)

print("Unpickled object:", loaded)
# Output: Unpickled object: {'topic': 'serialization', 'type': 'pickle'}
