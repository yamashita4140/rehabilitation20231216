# Pythonの教科書 2章

# 文字列
# ダブルクォートで文字列を表現
print("Hello,Python!!")
# シングルクォートで文字列を表現
print('Hello,Python!!')

# シングルクォートを文字列の中で使う
print("I can't speak English.")
# ダブルクォートを文字列の中で使う
print('He said,"I play the piano".')
# エスケープシーケンス
print('I can\'t speak English.')
print("I like \"Orange\".")

# # 三重引用符
# str = """
# 本日は晴天なり。
# 明日は明日の風が吹きます。
# 昨日のことは覚えていません。
# """
# print(str)

# 文字列同士の連結
# 文字列同士を連結する
s = "Hello," + "World!!"
print(s)
# 変数に入れた文字列同士を結合する
s1 = "Hello,"
s2 = "World!!!"
s3 = s1 + s2
print(s3)

# 文字列に変数の値を埋め込む
# 数値は文字列に変換しないと結合に使えない
kion_i = 30
kion = str(kion_i)
print("今日の気温は、" + kion + "度です。")

name = "Joro"
age = 19
desc = name + "は今年で" + str(age) + "歳です"
print(desc)

# format()を使う
per_inch = 2.54
inch = 24
cm = inch * per_inch
desc = "{}インチ={}センチ".format(inch, cm)
print(desc)

print("私は{name}です。".format(name="みどり"))
fmt = "年齢は{age}歳で、{job}をやっています。"
s = fmt.format(age=22, job="ぷーたろー")
print(s)
