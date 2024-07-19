class animal:
    def __init__(self,name,legs):
        print("ox has 4 legs")
        self.name = name
        self.legs = legs

    def info(self):
        print(f"{self.name} has {self.legs} legs")

a = animal("tiger","4")
a.info()



