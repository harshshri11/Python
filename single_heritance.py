class animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        print(f"animal is {self.name}")

class mammale:
    def __init__(self, type_animal):
        self.type_animal = type_animal
    def type(self):
        print(f"animal is {self.type_animal}")

class cat(animal, mammale):
    def __init__(self, name, type_animal):
        self.name = name
        self.type_animal = type_animal

c = cat("pussy", "mammale")
print(c.name, c.type_animal)
#print(cat.mro())

