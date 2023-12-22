# 写経12章 オブジェクト指向プログラミング


class Orange:  # Orangeクラスの定義
    def __init__(self, w, c):
        """weight(重さ)はグラム"""
        self.weight = w  # インスタンス変数 weight(重さ)
        self.color = c  # インスタンス変数 color(色)
        self.mold = 0  # インスタンス変数 mold(腐り性質 日数*平均温度)
        print("Created!")

    def rot(self, days, temp):  # rotメソッド(腐り性質の計算)
        """temp(温度)は摂氏"""
        self.mold = days * temp


orange = Orange(w=60, c="orange")
print(orange.mold)
orange.rot(days=10, temp=37)  # インスタンスorangeのrotメソッド呼び出し
print(orange.mold)

# # クラスのインスタンス化
# orl = Orange(w=10, c="dark orange")  # インスタンス化の際に、weightとcolorに初期値を与えている
# # print(orl)
# print(orl.weight)  # インスタンス変数 weightの初期値表示
# print(orl.color)  # インスタンス変数 colorの初期値表示
#
# orl.weight = 100  # インスタンス変数 weightの更新
# orl.color = "light orange"  # インスタンス変数 colorの更新
# print(orl.weight)  # 更新したインスタンス変数 weightの値の表示
# print(orl.color)  # 更新したインスタンス変数 colorの値の表示
#
# orl2 = Orange(w=60, c="dark orange")
# print(orl2.weight)
# print(orl2.color)
# orl3 = Orange(w=55, c="yellow")
# print(orl3.weight)
# print(orl3.color)
