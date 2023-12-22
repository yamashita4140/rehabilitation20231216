# 写経14章 特殊メソッド

class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):  # __repr__メソッドをオーバーライド -> 表示内容を変更する
        return self.name


lion = Lion("Dilbert")
print(lion)
