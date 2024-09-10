from deck import Deck
from Player import Player
class Game:
    def __init__(self, numOfDecks):
        self.players = []
        self.players.append(Player('Dealer', 1000000))
        self.givingDeck = Deck(numOfDecks)
        self.recyclingDeck = Deck(0)

    def start(self):
        self.dealForAll()
        self.dealForAll()
        return


    def gameReport(self):
        for plyr in self.players:
            plyr.report()

    def getDealer(self):
        return Player[0]
    def dealForAll(self):
        for plyr in self.players:
            plyr.takeCard(self.givingDeck.pop())

    def addPlayer(self, plyr):
        self.players.append(plyr)

    def removePlayer(self, plyer):
        self.players.remove(plyer)


