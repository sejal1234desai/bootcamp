# 05_yaml_serialize_car.py

import yaml

class Car:
    def __init__(self, make, model, year, owner):
        self.make = make
        self.model = model
        self.year = year
        self.owner = owner

    def to_dict(self):
        return self.__dict__

# Create a Car instance
car = Car(
    make="Honda",
    model="City",
    year=2022,
    owner="Sejal Desai"
)

# Serialize to YAML
yaml_data = yaml.dump(car.to_dict(), sort_keys=False)

# Print the YAML string
print("Car object in YAML format:")
print(yaml_data)

# Write to file
with open("car_data.yaml", "w") as f:
    f.write(yaml_data)
