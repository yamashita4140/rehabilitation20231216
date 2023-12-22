# 写経14章 クラス変数とインスタンス変数

class Rectangle:
    def __init__(self, w, l):
        self.width = w  # インスタンス変数
        self.length = l  # インスタンス変数

    def print_size(self):
        print("{} by {}".format(self.width, self.length))


my_rectangle = Rectangle(w=10, l=25)
my_rectangle.print_size()
