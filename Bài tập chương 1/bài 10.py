import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Ellipse(Point):
    def __init__(self, x, y, a, b):
        super().__init__(x, y)
        self.a = a  # bán trục lớn
        self.b = b  # bán trục nhỏ

    def area(self):
        return math.pi * self.a * self.b

class Circle(Ellipse):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius, radius)

ellipse = Ellipse(0, 0, 5, 3)
print("Diện tích elip:", ellipse.area())

circle = Circle(0, 0, 4)
print("Diện tích đường tròn:", circle.area())
