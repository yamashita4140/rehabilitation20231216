# Pythonの教科書 2章5
# 分岐 if文
# 閏年の判定

year = int(input("西暦何年?:"))
is_leap = False  # 判定用変数(Boolean型)の初期値を"False"に設定
if year % 400 == 0:
    is_leap = True
elif year % 100 == 0:
    is_leap = False
elif year % 4 == 0:
    is_leap = True

if is_leap:
    print("閏年です")
    # print("平年です")
else:
    print("平年です")
    # print("閏年です")
