# 写経13章 継承

class Shape:
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def print_size(self):
        print("{} by {}".format(self.width, self.length))


my_shape = Shape(w=10, l=20)
my_shape.print_size()
