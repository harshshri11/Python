class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def from_string(cls, string):
        name, age = string.split('-')
        return cls(name, int(age))
Person = person.from_string("harsh-20")
print(Person.name, Person.age)
