# 第10章 ハングマン

import hangman
import random

word_list = ["tomcat", "thunder", "bombcat", "hornet", "fantom"]
random_word = random.choice(word_list)  # リストからランダムでチョイス

hangman.hangman(random_word)
