# 06_yaml_deserialize_car.py

import yaml

class Car:
    def __init__(self, make, model, year, owner):
        self.make = make
        self.model = model
        self.year = year
        self.owner = owner

    @classmethod
    def from_yaml(cls, yaml_string):
        data = yaml.safe_load(yaml_string)
        return cls(**data)

    def __str__(self):
        return f"{self.year} {self.make} {self.model} owned by {self.owner}"

# Read YAML data from file
with open("car_data.yaml", "r") as f:
    yaml_data = f.read()

# Convert YAML string to Car object
car = Car.from_yaml(yaml_data)

# Print the car details
print("Deserialized Car object:")
print(car)
