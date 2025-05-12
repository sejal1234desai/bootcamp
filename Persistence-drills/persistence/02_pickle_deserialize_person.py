# 02_pickle_deserialize_person.py

# 02_pickle_deserialize_person.py

import pickle
from person_model import Person  # Needed for pickle to locate the class

with open("person_data.pkl", "rb") as f:
    sejal = pickle.load(f)

print("Deserialized Person object:")
print(f"Name: {sejal.name}")
print("Educational Institutions:")
for edu in sejal.educational_institutions:
    print(f"  - {edu}")
print("Colleagues:")
for colleague in sejal.colleagues:
    print(f"  - {colleague}")
