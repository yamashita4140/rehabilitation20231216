# # Pythonの教科書 2章4
# # ユーザから入力を得る
#
# # 名前を入力して出力
# name = input("Input your name: ")
# print(name + "さん、こんにちは!!")
#
# # 数値を入力する
# per_inch = 2.54
# inch = float(input("inch?:"))
# cm = inch * per_inch
# desc = ("{}inch = {}cm".format(inch, cm))
# print(desc)

# 単位変換 カラット -> グラム
per_ct = 0.2
ct = float(input("何カラットですか?:"))
g = ct * per_ct
desc = "{}カラット = {}グラム".format(ct, g)
print(desc)

# 時給計算
jikyu = int(input("時給はいくらですか?:"))
jikan = int(input("何時間働きましたか?:"))
kyuuryou = jikan * jikyu
fmt = """
時給{jikyu}円で、{jikan}時間働いたので。。。
給料は{kyuuryou}円です。
"""
desc = fmt.format(jikyu=jikyu, kyuuryou=kyuuryou, jikan=jikan)
print(desc)
