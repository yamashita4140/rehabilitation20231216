# Pythonの教科書 2章4
# ユーザから入力を得る

# 名前を入力して出力
name = input("Input your name: ")
print(name + "さん、こんにちは!!")

# 数値を入力する
per_inch = 2.54
inch = float(input("inch?:"))
cm = inch * per_inch
desc = ("{}inch = {}cm".format(inch, cm))
print(desc)
