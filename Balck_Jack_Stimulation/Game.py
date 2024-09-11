import random

from deck import Deck
from Player import Player


class Game:
    def __init__(self, shoeSize=4):
        self.dealer = Player("John the Faithful Dealer", 10000, dealer=True)
        self.players = []
        self.shoe = Deck(shoeSize)
        self.usedCards = Deck(0)

    def run(self):
        while True:
            # the initial two cards
            for i in range(2):
                for p in self.players:
                    p.receiveCard(self.shoe.pop())

                self.dealer.receiveCard(self.shoe.pop())

            # individual deal or stand

            for p in self.players:
                while not p.bust():
                    match p.action():
                        case "hit":
                            p.receiveCard(self.shoe.pop(0))
                        case "stand":
                            break
                        # case split etc
                        case _:
                            break

                if p.bust():
                    p.fund -= p.bet
                    self.players[0].fund += p.bet
                    # recycle cards

            while self.dealer.action() == "hit":
                self.players[0].receiveCard(self.deck.pop())

            if self.dealer.bust():
                for p in self.players:
                    if not p.bust():
                        self.dealer.fund -= p.bet
                        p.fund += p.bet
            else:
                for p in self.players:
                    if max(p.handValue()) > max(self.dealer.handValue()):
                        self.dealer.fund - p.bet
                        p.fund += p.bet

            return




    def gameReport(self):
        for plyr in self.players:
            plyr.report()

    def addPlayer(self, plyr):
        self.players.append(plyr)

    def removePlayer(self, plyer):
        self.players.remove(plyer)
