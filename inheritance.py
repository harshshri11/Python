class cycle:
    def __init__(self,wheels,engine):
        self.wheels = wheels
        self.engine = engine

    def showdetail(self):
        print(f"cycle has {self.wheels} wheels and  {self.engine}")

class bike(cycle):
        def show(self):
            print(f"bike has {self.wheels} wheels and also has {self.engine}")

a = cycle(2,"no engine")
a.showdetail()
b = bike(2, "engine")
b.show()

