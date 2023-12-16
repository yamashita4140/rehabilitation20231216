# 第10章 ハングマン

def hangman(word):
    wrong = 0
    stages = ["",
              "_________          ",
              "|                  ",
              "|         |        ",
              "|         0        ",
              "|        /|\       ",
              "|        / \       ",
              "|                  "]
    rletters=list(word)
    board=["_"] * len(word)
    win=False
    print("ハングマンへようこそ!")
