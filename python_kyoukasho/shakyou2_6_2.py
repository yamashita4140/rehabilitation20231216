# Pythonの教科書 2章6
# 繰り返し for文
# nからmまでを足すと?
n = int(input("始まりの値: "))
m = int(input("終わりの値: "))
sum = 0
for i in range(n, m + 1):
    sum += i
    print(i, "を足すと", sum)
print("{}から{}まで足すと{}".format(n, m, sum))
