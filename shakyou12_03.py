# 写経12章 オブジェクト指向プログラミング

class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def area(self):  # areaメソッド(面積計算)
        return self.width * self.length

    def change_size(self, w, l):  # change_sizeメソッド(サイズ変更)
        self.width = w
        self.length = l


rectangle = Rectangle(w=10, l=20)  # インスタンスの生成
print(rectangle.area())  # areaメソッドの呼び出し(面積計算)
rectangle.change_size(w=40, l=15)  # インスタンス変数の変更
print(rectangle.area())  # areaメソッドの呼び出し(面積計算)
