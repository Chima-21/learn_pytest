from dataclasses import dataclass


@dataclass
class Employee:
    firstname: str
    lastname: str
    age: str
    unit: str

    def __post_init__(self):
        self.email = f"{self.firstname.lower()}.{self.lastname.lower()}@chimaio.com"
        self.unit = self.unit.upper()
        self.firstname = self.firstname.title()
        self.lastname = self.lastname.title()

    def __str__(self):
        return f"Staff {self.lastname} is in {self.unit} unit"
