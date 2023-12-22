# 第12章 チェレンジ4

class Hexagon:
    def __init__(self, l):
        self.length = l

    def calculate_perimeter(self):
        return self.length * 6


hexagon = Hexagon(l=25)
print(hexagon.calculate_perimeter())
