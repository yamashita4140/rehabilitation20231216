# 写経12章 オブジェクト指向プログラミング


class Orange:  # Orangeクラスの定義
    def __init__(self, w, c):
        self.weight = w  # インスタンス変数 weight(重さ)
        self.color = c  # インスタンス変数 color(色)
        print("Created!")


# クラスのインスタンス化
orl = Orange(w=10, c="dark orange")  # インスタンス化の際に、weightとcolorに初期値を与えている
# print(orl)
print(orl.weight)  # インスタンス変数 weightの初期値表示
print(orl.color)  # インスタンス変数 colorの初期値表示

orl.weight = 100  # インスタンス変数 weightの更新
orl.color = "light orange"  # インスタンス変数 colorの更新
print(orl.weight)  # 更新したインスタンス変数 weightの値の表示
print(orl.color)  # 更新したインスタンス変数 colorの値の表示
