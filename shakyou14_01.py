# 写経14章 クラス変数とインスタンス変数

class Rectangle:
    recs = []  # クラス変数

    def __init__(self, w, l):
        self.width = w  # インスタンス変数
        self.length = l  # インスタンス変数
        self.recs.append((self.width, self.length))  # インスタンスが生成れるたびに、クラス変数に追加を行う

    def print_size(self):
        print("{} by {}".format(self.width, self.length))


# my_rectangle = Rectangle(w=10, l=25)
# my_rectangle.print_size()
r1 = Rectangle(w=10, l=25)
r1.print_size()
print(r1.recs)
r2 = Rectangle(w=30, l=10)
r2.print_size()
print(r2.recs)
r3 = Rectangle(w=20, l=15)
r3.print_size()
print(r3.recs)

print(Rectangle.recs)  # クラス変数の出力
