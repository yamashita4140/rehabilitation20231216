# 第10章 ハングマン

def hangman(word):
    wrong = 0   # wrong=間違いカウンタ
    stages = ["",
              "_________          ",
              "|                  ",
              "|         |        ",
              "|         0        ",
              "|        /|\       ",
              "|        / \       ",
              "|                  "]
    rletters = list(word)   # 正解文字列を分解してリストにしたもの
    board = ["_"] * len(word)   # ヒント及び正解を表示するためのボード
    win = False # 終了フラグ
    print("ハングマンへようこそ!")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね"
        char = input(msg)
        if char in rletters:    # 入力文字が、正解の中にあるかを判定する
            cind = rletters.index(char) # 該当する文字位置を取り出す
            board[cind] = char  # ボードの該当位置をめくる
            rletters[cind] = "$"    # 正解位置を$に置き換える(正解が二文字ある場合の対策)
        else:
            wrong += 1  # 間違いカウンタを増加
        print(" ".join(board))  # ボードを表示する
        e = wrong + 1   # ステージを表示する
        print("\n".join(stages[0:e]))
        if "_" not in board:    # 勝利判定(ボードがすべてめくられているか?)
            print("あなたの勝ち!")
            print(" ".join(board))  # 正解を表示
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong + 1]))
        print("あなたの負け!正解は {}.".format(word))


hangman("cact")
