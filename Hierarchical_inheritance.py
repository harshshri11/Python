class Human:
    def __init__(self, name):
        self.name = name
class employee(Human):
    def __init__(self, name, id):
        Human.__init__(self, name)
        self.id = id
    def show_details(self):
        print(f"employee name is {self.name} and id is {self.id}")
class lebur(Human):
    def __init__(self, name, payement):
        Human.__init__(self, name)
        self.payement = payement
    def show_datails(self):
        print(f"labur name is {self.name} and payement of per day he gets {self.payement}")
class programmer(employee):
    def __init__(self, name, id, lang):
        employee.__init__(self, name, id)
        self.lang = lang
    def show_details(self):
        print(f"progeammer name is {self.name} and id is {self.id} language he learn {self.lang}")

p = programmer("harsh", 1213, "python")
p.show_details()