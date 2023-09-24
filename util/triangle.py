from util.shape import Shape


class Triangle(Shape):
    def __init__(self, base, height):
        self.tri_area = 0.0
        self.base = base
        self.height = height

    def area(self):
        self.tri_area = (self.base * self.height) / 2
        return self.tri_area

    def __str__(self) -> str:
        self.area()
        return 'Triangle Area of ' + str(self.base) + 'U x ' + str(self.height) + 'U :' + str(self.tri_area)
