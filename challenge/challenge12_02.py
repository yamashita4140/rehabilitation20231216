# 第12章 チェレンジ2

# mathモジュール↓
# https://docs.python.org/ja/3/library/math.html

import math


class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return math.pow(self.radius, 2) * math.pi


circle = Circle(r=20)
print(circle.area())
