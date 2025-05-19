Persistence Drills
This project demonstrates different ways to handle persistence in Python, covering serialization, deserialization, and managing custom collections, cyclic references, and more. The drills include exercises using Pickle, JSON, YAML, and custom serialization techniques.


Folder Structure
persistence/: Contains the individual Python scripts for each persistence task.

01_pickle_serialize_person.py: Serialize a Person object using Pickle.

02_pickle_deserialize_person.py: Deserialize the serialized Person object.

03_json_serialize_book.py: Convert a Book object to a JSON string.

04_json_deserialize_book.py: Deserialize a Book object from a JSON string.

05_yaml_serialize_car.py: Serialize a Car object to YAML format.

06_yaml_deserialize_car.py: Deserialize a Car object from YAML format.

07_custom_serialize_graph.py: Serialize a Graph object with complex data structures.

08_skip_sensitive_data_serialize.py: Serialize a User object while skipping sensitive attributes.

09_game_state_persistence.py: Save and restore the state of a game session.

10_versioned_object_handling.py: Handle versioning of serialized objects (e.g., upgrading from PersonV1 to PersonV2).

11_serialize_custom_collection.py: Serialize a custom collection class (MyCollection).

12_serialize_cyclic_references.py: Handle cyclic references during serialization.


1. Create a Virtual Environment
Use the following command to create a virtual environment named venv in your project folder:

bash
uv venv venv

How to Run

python3 <script_name>.py
python3 01_pickle_serialize_person.py


Expected Output
01 - Serialize Person Object (Pickle)
Script: 01_pickle_serialize_person.py
Description: Serialize a Person object with attributes like name, educational_institutions, and colleagues using Pickle.
Expected Output:
Person object serialized successfully to 'person_data.pkl'

02 - Deserialize Person Object (Pickle)
Script: 02_pickle_deserialize_person.py
Description: Deserialize the Person object created in the previous task.
Expected Output:
Deserialized Person object:
Name: Sejal Desai
Educational Institutions:
  - S.S. High School, Adkur
  - M.R. College, Gadhinglaj
  - Shivaji University, Kolhapur (B.Sc. and M.Sc. in Computer Science)
Colleagues:
  - Rahul Patil
  - Sneha Kulkarni
  - Amit Jadhav

03 - Serialize Book Object (JSON)
Script: 03_json_serialize_book.py
Description: Convert a Book object to a JSON string.
Expected Output:
Book object serialized successfully to 'book_data.json'

04 - Deserialize Book Object (JSON)
Script: 04_json_deserialize_book.py
Description: Deserialize a Book object from the JSON file created in the previous task.
Expected Output:
Deserialized Book object:
Title: Python Programming
Author: Sejal Desai
Year: 2023

05 - Serialize Car Object (YAML)
Script: 05_yaml_serialize_car.py
Description: Serialize a Car object to YAML format.
Expected Output:
Car object serialized successfully to 'car_data.yaml'

06 - Deserialize Car Object (YAML)
Script: 06_yaml_deserialize_car.py
Description: Deserialize a Car object from the YAML file created in the previous task.
Expected Output:
Deserialized Car object:
Make: Tesla
Model: Model 3
Year: 2023

07 - Custom Serialization for Graph
Script: 07_custom_serialize_graph.py
Description: Serialize a Graph object that contains nodes and edges.
Expected Output:
Graph object serialized successfully to 'graph_data.pkl'

08 - Skipping Sensitive Data During Serialization
Script: 08_skip_sensitive_data_serialize.py
Description: Serialize a User object while excluding sensitive data.
Expected Output:
User object serialized successfully (excluding sensitive attributes).

09 - Save and Restore Game State
Script: 09_game_state_persistence.py
Description: Save and restore the state of a game session to and from a file.
Expected Output:
Game state saved successfully.
Game state loaded successfully:
Current Score: 120
Level: 3

10 - Versioned Object Handling
Script: 10_versioned_object_handling.py
Description: Handle version changes in serialized objects, upgrading from PersonV1 to PersonV2.
Expected Output:
PersonV1 object serialized successfully.
Deserialized PersonV1 object
PersonV2: Sejal Desai, Age: 25, Email: sejaldesai2001@gmail.com

11 - Serialize Custom Collection
Script: 11_serialize_custom_collection.py
Description: Serialize a custom collection class (MyCollection).
Expected Output:
MyCollection object serialized successfully.
Deserialized collection:
MyCollection contains: ['Sejal Desai', 'Rahul Patil', 'Amit Jadhav']

12 - Serialize Cyclic References
Script: 12_serialize_cyclic_references.py
Description: Handle cyclic references during serialization and deserialization.
Expected Output:
Objects with cyclic references serialized successfully.
Deserialized person with cyclic references:
Person(Sejal Desai)
Sejal Desai's friend is: Rahul Patil

