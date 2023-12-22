# 第13章 チャレンジ1 -> チャレンジ3

class Shape:
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def what_am_i(self):
        return "I am a shape"


class Rectangle(Shape):
    # def __init__(self, w, l):
    #     self.width = w
    #     self.length = l

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2


class Square(Shape):
    # def __init__(self, w, l):
    #     self.width = w
    #     self.length = l

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2


rectangle = Rectangle(w=15, l=20)
print(rectangle.calculate_perimeter())
print(rectangle.what_am_i())
square = Square(w=20, l=20)
print(square.calculate_perimeter())
print(square.what_am_i())
