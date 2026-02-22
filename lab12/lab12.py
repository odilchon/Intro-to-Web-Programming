class Human:
    def __init__(self, full_name, years):
        self.full_name = full_name
        self.years = years

    def greet(self):
        print(f"Hi, I am {self.full_name}")

    def __repr__(self):
        return f"{self.full_name} - {self.years} years"

person1 = Human("John", 20)
print(person1.full_name)
print(person1.years)

person2 = Human("John", 20)
print(person2)

person3 = Human("Mike", 36)
person3.greet()

class HumanAlt:
    def __init__(self, name_value, age_value):
        self.name_value = name_value
        self.age_value = age_value

    def greet(self):
        print(f"My name is {self.name_value}")

another = HumanAlt("John", 20)
another.greet()