# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from simple_poker import SimplePoker
from poker_player import PokerPlayer

if __name__ == '__main__':
    s = SimplePoker(100,5,PokerPlayer,PokerPlayer)
    sm = 0.0
    n = 10000000
    for i in range(n):
        sm += s.play_game()
    print(sm/n)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
