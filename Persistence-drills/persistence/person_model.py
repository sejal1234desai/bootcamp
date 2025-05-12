# person_model.py

class Person:
    def __init__(self, name, educational_institutions, colleagues):
        self.name = name
        self.educational_institutions = educational_institutions
        self.colleagues = colleagues

    def __str__(self):
        return f"Person(name={self.name}, educational_institutions={self.educational_institutions}, colleagues={self.colleagues})"
