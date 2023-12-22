# 第12章 チェレンジ3

class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h

    def area(self):
        return self.base * self.height / 2


triangle = Triangle(b=10, h=15)
print(triangle.area())
