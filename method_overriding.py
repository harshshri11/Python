class shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def area(self):
        return self.x*self.y
class circle(shape):
    def __init__(self, redius):
        self.redius = redius
        super().__init__(redius,redius)
    def area(self):
        return 3.14* super().area()
sq = shape(3, 5)
print(sq.area())
crc = circle(6)
print(crc.area())