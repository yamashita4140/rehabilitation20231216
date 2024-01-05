# Pythonの教科書 2章5
# 分岐 if文
# BMI判定
# if ~elifを使って
weight = float(input("体重は何Kg?:"))
height = float(input("身長は何cm?:"))
height = height / 100
bmi = weight / (height ** 2)

result = ""
if bmi < 18.5:
    result = "痩せ型"
elif bmi < 25:
    result = "標準体重"
elif bmi < 30:
    result = "肥満(軽)"
else:
    result = "肥満(重)"
print("BMI: ", bmi)
print("判定: ", result)
