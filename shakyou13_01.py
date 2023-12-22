# 写経13章 継承

class Shape:
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def print_size(self):
        print("{} by {}".format(self.width, self.length))


class Square(Shape):  # Shapeクラスを継承してSquareクラスを定義
    def area(self):     # Squareクラス独自のareaメソッドを追加
        return self.width*self.length

    def print_size(self):   # メソッドのオーバーライド
        print("I am {} by {}".format(self.width,self.length))



a_square = Square(w=30, l=30)
a_square.print_size()   # オーバーライドしたメソッドの呼び出し
print(a_square.area())  # Squareクラスに追加したareaメソッドの呼び出し



# my_shape = Shape(w=10, l=20)
# my_shape.print_size()
