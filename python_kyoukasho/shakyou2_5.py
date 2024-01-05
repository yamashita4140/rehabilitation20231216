# Pythonの教科書 2章5
# 分岐 if文

# チケット売り場のレジシステム
# 子供料金:500円/人
# 通常料金:1000円/人
# 年配者料金:700円/人
# 団体割引:10人以上で2割引

# 人数の入力
children = int(input("子供料金(13歳未満)は何人?:"))
normal = int(input("通常料金(13歳〜64歳)は何人?:"))
elder = int(input("年配者料金(65歳以上)は何人?:"))

total_num = children + normal + elder
children_price = children * 500
normal_price = normal * 1000
elder_price = elder * 700
total_price = children_price + normal_price + elder_price

if total_num >= 10:
    print("団体割引があります")
    total_price *= 0.8
else:
    print("団体割引はありません")

print("子供料金　:{}人 ✕ 500 = {}円".format(children, children_price))
print("通常料金　:{}人 ✕1000 = {}円".format(normal, normal_price))
print("年配者料金:{}人 ✕ 700 = {}円".format(elder, elder_price))
print("合計:{}人 {}円".format(total_num, int(total_price)))
