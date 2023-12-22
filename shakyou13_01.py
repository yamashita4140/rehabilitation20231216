# 写経13章 継承

class Shape:
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def print_size(self):
        print("{} by {}".format(self.width, self.length))


class Square(Shape):  # Shapeクラスを継承してSquareクラスを定義
    pass


a_square = Square(w=30, l=30)
a_square.print_size()   # 親クラスから継承したprint_sizeメソッドの呼び出し

# my_shape = Shape(w=10, l=20)
# my_shape.print_size()