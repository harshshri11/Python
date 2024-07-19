class Human:
    def __init__(self, name):
        self.name = name
class employee(Human):
    def __init__(self, name, id, salary):
        Human.__init__(self, name)
        self.id = id
        self.salary = salary
    def show_details(self):
        print(f"name of employee is {self.name} and id of employee is {self.id} salary of employee is {self.salary}")
class programmer(employee):
    def __init__(self, name, id, salary, language):
        employee.__init__(self, name, id, salary)
        self.language = language
    def show_details(self):
        print(f"name of programmer is {self.name} and id of programmer is {self.id} salary of programmer is {self.salary} language learn by programmer is {self.language}")
e = employee("Raj mali", 123, 20000)
e.show_details()

p = programmer("harsh", 1111, 50000, "python")
p.show_details()