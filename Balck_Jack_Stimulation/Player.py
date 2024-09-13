import random

from card import Card


class Player:
    def __init__(self, name, fund, dealer=False):
        self.name = name
        self.fund = fund
        self.hand = []
        self.dealer = dealer
        self.bet = 5

    def bust(self) -> bool:
        return min(self.handValue()) > 21

    def action(self) -> str:
        # dealer policy
        if self.dealer:
            if min(self.handValue()) < 17:
                return "hit"
            else:
                return "stand"

        # player policy
        if max(self.handValue()) < 18:
            return "hit"

        return "stand"

    def receiveCard(self, card: Card):
        self.hand.append(card)

    def report(self):
        print(self.name, self.fund, [card.getCard() for card in self.hand])

    def handValue(self) -> (int, int):
        # if soft value exist, it will be hard val + 10

        # implemented this way coz soft value is important sometimes
        # it's used when deciding to hit or stand, or deciding win or lose

        val = 0
        ace = False

        for c in self.hand:
            if c.num in ['J', 'Q', 'K']:
                val += 10
            elif c.num == 'A':
                val += 1
                ace = True
            else:
                val += int(c.num)

        if ace and val + 10 <= 21:
            return val, val + 10

        # else
        return val, val

    def modifyFund(self, amount):
        self.fund += amount
