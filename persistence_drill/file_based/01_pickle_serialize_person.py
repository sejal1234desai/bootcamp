# 01_pickle_serialize_person.py

# 01_pickle_serialize_person.py

import pickle
from person_model import Person

sejal = Person(
    name="Sejal Desai",
    educational_institutions=[
        "S.S. High School, Adkur",
        "M.R. College, Gadhinglaj",
        "Shivaji University, Kolhapur (B.Sc. and M.Sc. in Computer Science)"
    ],
    colleagues=["Rahul Patil", "Sneha Kulkarni", "Amit Jadhav"]
)

with open("person_data.pkl", "wb") as f:
    pickle.dump(sejal, f)

print("Person object serialized successfully to 'person_data.pkl'")
