# Pythonの教科書 2章6
# 繰り返し While文

# エネルギーが尽きるまで走り続ける
energy = int(input("エネルギーを充填せよ:"))
while energy > 0:
    print("+走る")
    print("|energy = ", energy)
    energy -= 1
print("+ガス欠")
