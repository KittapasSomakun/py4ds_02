import math
from util.shape import Shape


class Ellipse(Shape):

    def __init__(self, radius_x_axis, radius_y_axis):
        self.ellipse_area = 0.0
        self.radius_x = radius_x_axis
        self.radius_y = radius_y_axis

    def area(self):
        self.ellipse_area = math.pi * self.radius_x * self.radius_y
        return self.ellipse_area

    def __str__(self) -> str:
        self.area()
        return 'Ellipse Area of ' + str(self.radius_x) + 'U x ' + str(self.radius_y) + 'U :' + str(self.ellipse_area)
