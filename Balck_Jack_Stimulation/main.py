from Game import Game
from Player import Player
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    game = Game(3)
    game.addPlayer(Player("Swift", 500))
    game.addPlayer(Player("Rupert", 1000))
    game.addPlayer(Player("Carlito", 1000))

    game.start()
    game.gameReport()











# See PyCharm help at https://www.jetbrains.com/help/pycharm/
