class Triangle:
    def __init__(self, a, b, c):
        self.a = a  # Cạnh 1
        self.b = b  # Cạnh 2
        self.c = c  # Cạnh 3
    
    def perimeter(self):
        #Tính chu vi tam giác.
        return self.a + self.b + self.c

    def area(self):
        #Tính diện tích tam giác bằng công thức Heron.
        s = self.perimeter() / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5


class RightTriangle(Triangle):
    def __init__(self, a, b):
        # Cạnh huyền được tính từ a và b
        super().__init__(a, b, (a**2 + b**2) ** 0.5)

    def area(self):
        #Tính diện tích tam giác vuông.
        return (self.a * self.b) / 2


class IsoscelesTriangle(Triangle):
    def __init__(self, base, equal_side):
        # Hai cạnh bằng nhau (equal_side) và một cạnh đáy (base)
        super().__init__(equal_side, equal_side, base)

    def area(self):
        #Tính diện tích tam giác cân."""
        height = (self.a**2 - (self.b / 2) ** 2) ** 0.5
        return (self.b * height) / 2


class EquilateralTriangle(IsoscelesTriangle):
    def __init__(self, side):
        # Tất cả các cạnh đều bằng nhau
        super().__init__(side, side)

    def area(self):
        #Tính diện tích tam giác đều."""
        return (self.a ** 2 * (3 ** 0.5)) / 4


# Tạo và sử dụng các đối tượng
triangle = Triangle(3, 4, 5)
print("Tam giác thường:")
print("Chu vi:", triangle.perimeter())
print("Diện tích:", triangle.area())

right_triangle = RightTriangle(3, 4)
print("\nTam giác vuông:")
print("Chu vi:", right_triangle.perimeter())
print("Diện tích:", right_triangle.area())

isosceles_triangle = IsoscelesTriangle(6, 5)
print("\nTam giác cân:")
print("Chu vi:", isosceles_triangle.perimeter())
print("Diện tích:", isosceles_triangle.area())

equilateral_triangle = EquilateralTriangle(6)
print("\nTam giác đều:")
print("Chu vi:", equilateral_triangle.perimeter())
print("Diện tích:", equilateral_triangle.area())
