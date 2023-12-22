# 第12章 チェレンジ1

class Apple:
    def __init__(self, w, c, pr, pda):
        self.weight = w
        self.color = c
        self.price = pr
        self.producing_area = pda


apple1 = Apple(w=30, c="red", pr=120, pda="Aomori")
print(apple1.weight, apple1.color, apple1.price, apple1.producing_area)
apple2 = Apple(w=40, c="light red", pr=100, pda="U.S.A.")
print(apple2.weight, apple2.color, apple2.price, apple2.producing_area)
