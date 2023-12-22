# 写経12章 手続き型プログラミング

# グローバル変数(リスト)
# 関数collect_songs()から直接書き換えられる
pop = []  # 洋楽ポップソングを保存するリスト
jpop = []  # JPopソングを保存するリスト


def collect_songs():
    song = "曲名を入力してください: "
    ask = ("p か j のどちらかを入力してください。qで終わります: ")

    while True:
        genre = input(ask)
        if genre == "q":
            break
        if genre == "p":
            p = input(song)
            pop.append(p)

        elif genre == "j":
            j = input(song)
            jpop.append(j)

        else:
            print("不正な値です。")

    print("pop songs: ", pop)
    print("jpop songs: ", jpop)


collect_songs()
