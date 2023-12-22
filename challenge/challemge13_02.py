# 第13章 チャレンジ1

class Square:
    def __init__(self, w):
        self.width = w

    def print_size(self):
        print("I am {} by {}".format(self.width, self.width))

    def change_size(self, values):
        self.width += values


square = Square(w=256)
square.print_size()
c_values = int(input("サイズ変更値: "))
square.change_size(values=c_values)
square.print_size()
