class React:
    def __init__(self, width, height):
        self.rect_area = 0.0
        self.width = width
        self.height = height

    def area(self):
        self.rect_area = self.width * self.height
        return self.rect_area

    def __str__(self) -> str:
        return 'Rectangle Area of ' + str(self.width) + 'U x ' + str(self.height) + 'U :' + str(self.area())
