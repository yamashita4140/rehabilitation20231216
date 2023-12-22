# 第13章 チャレンジ1

class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2


class Square:
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2


rectangle = Rectangle(w=15, l=20)
print(rectangle.calculate_perimeter())
square = Square(w=20, l=20)
print(square.calculate_perimeter())
