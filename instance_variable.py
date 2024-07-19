class employee:
    class_variable = "amezone"
    def __init__(self,name):
        self.name = name
    def showdetails(self):
        print(f"employee name is {self.name} class variable is {self.class_variable}")
a = employee("harsh")
print(a.class_variable)
print(a.name)
