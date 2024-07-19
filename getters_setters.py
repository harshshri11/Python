class get_set:
    def __init__(self):
        self.name = ""
        self.age = 0

    def get_name(self):
        self.name = input("enter the name:")
        self.age = int(input("enter the age:"))

    def set_name(self):
        print(f"{self.name}_{self.age}")

get_set = get_set()
get_set.get_name()
get_set.set_name()