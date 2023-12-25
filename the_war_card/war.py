# 15章 戦争

from random import shuffle


class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]
    # スート(カードの種類)の定義 最弱はスペード、最強はクラブ

    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10",
              "Jack", "Queen", "King", "Ace"]

    # カードの値の定義 0番、1番は未使用。添字の値がそのままカードの強さになる

    def __init__(self, v, s):   # カードの生成
        """スートも値も整数値"""
        self.value = v
        self.suit = s

    def __lt__(self, c2):   # 特殊メソッド 相手と比較して自分が小さければ True を返す
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.value < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):   # 特殊メソッド 相手と比較して自分が大きければ True を返す
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self): # 出力時にスートと値を出力する
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v


class Deck:
    def __init__(self):
        self.cards = []     # デッキのリスト
        # カードの生成(2重ループを使い、52枚のカードを生成)
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
                # 生成したカードインスタンスをリストに追加
        shuffle(self.cards)     # デッキをシャッフルする

    def rm_card(self):  # デッキの上(リストの先頭)から1枚ずつカードを取り出すメソッド
        if len(self.cards) == 0:
            return  # カードが1枚もなければNoneを返す
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


class Game:
    def __init__(self):
        name1 = input("Player1 Name: ")
        name2 = input("Player2 Name: ")
        self.deck = Deck()  # デッキインスタンスの生成
        self.p1 = Player(name1) # Player1インスタンスの生成
        self.p2 = Player(name2) # Player2インスタンスの生成

    def wins(self, winner): # 勝利者の出力メソッド
        w = "{} won this round."
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c): # 引いたカードの表示メソッド
        d = "{} draw {} and {} draw {}."
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("Start the war!!")

        while len(cards) >= 2:
            m = "If 'q' is entered, cease fire; any other key will continue the battle."
            response = input(m)
            if response == "q":
                break
            p1c = self.deck.rm_card()   # Player1がカードを1枚引く(デッキインスタンスのrm_cardメソッド)
            p2c = self.deck.rm_card()   # Player2がカードを1枚引く
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            # ラウンドの勝利判定
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)
        print("The war is over...{} is winning!".format(win))

    def winner(self, p1, p2):   # 勝者の名前を返すメソッド
        if p1.wins > p2.wins:
            return p1.name
        if p2.wins > p1.wins:
            return p2.name
        return "Draw!!"


game = Game()
game.play_game()
