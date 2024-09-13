import random

from deck import Deck
from Player import Player


class Game:
    def __init__(self, shoeSize=4):
        self.dealer = Player("Dealer", 10000, dealer=True)
        self.players = []
        self.shoe = Deck(shoeSize)
        self.usedCards = Deck(0)

    def run(self):
        while self.players:
            print("\r")

            # the initial two cards
            for i in range(2):
                for p in self.players:
                    p.receiveCard(self.shoe.pop())

                self.dealer.receiveCard(self.shoe.pop())

            # individual deal or stand
            for p in self.players:
                while not p.bust():
                    if p.action() == "hit":
                        p.receiveCard(self.shoe.pop())
                    else:
                        break

                if p.bust():
                    print(p.name + " busted")
                    p.fund -= p.bet
                    self.dealer.fund += p.bet
                    # recycle cards

            while self.dealer.action() == "hit":
                self.dealer.receiveCard(self.shoe.pop())


            # report section
            self.dealer.report()
            for p in self.players:
                p.report()


            if self.dealer.bust():
                for p in self.players:
                    if not p.bust():
                        print("Dealer bust")
                        self.dealer.fund -= p.bet
                        p.fund += p.bet
            else:
                for p in self.players:
                    playerHand = max(p.handValue())
                    dealerHand = max(self.dealer.handValue())

                    if p.bust():
                        continue

                    if playerHand == dealerHand:
                        print("tie")
                        continue
                    elif playerHand > dealerHand:
                        print(p.name + " won")
                        self.dealer.fund -= p.bet
                        p.fund += p.bet
                    else:
                        print(p.name + " lost")
                        self.dealer.fund += p.bet
                        p.fund -= p.bet


            for p in self.players:
                if p.fund <= 0:
                    self.removePlayer(p)



            # recycle the card
            # keeping a used card because
            # drawn card are available information to human and model
            # maybe more complex feature will be added, like a cut card

            for p in self.players:
                while p.hand:
                    self.usedCards.push(p.hand.pop())

            while self.dealer.hand:
                self.usedCards.push(self.dealer.hand.pop())

            if len(self.shoe.stack) < 20:
                self.shoe.stack.extend(self.usedCards.stack)
                self.usedCards.clear()
                random.shuffle(self.shoe.stack)



        return




    def gameReport(self):
        for plyr in self.players:
            plyr.report()

    def addPlayer(self, plyr):
        self.players.append(plyr)

    def removePlayer(self, plyer):
        self.players.remove(plyer)
