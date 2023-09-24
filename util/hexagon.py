import math
from util.shape import Shape


class Hexagon(Shape):

    def __init__(self, side):
        self.hex_area = 0.0
        self.side = side

    def area(self):
        self.hex_area = (3 * math.sqrt(3) * (self.side ** 2)) / 2
        return self.hex_area

    def __str__(self) -> str:
        self.area()
        return 'Hexagon Area of ' + str(self.side) + 'U :' + str(self.hex_area)
