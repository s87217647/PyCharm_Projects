class Player:
    def __init__(self, name, fund):
        self.name = name
        self.fund = fund
        self.hand = []
        self.hit = True

    def takeCard(self, card):
        self.hand.append(card)
        self.evaluateHand()

    def report(self):
        print(self.name, self.fund, self.hit, [card.getCard() for card in self.hand])

    def evaluateHand(self):
        if self.name == 'Swift':
            return
        elif self.name == 'Dealer':
            return
        else:
            return
    def displayHand(self):
        print(self.hand)
    def decreaseFund(self, amt):
        if amt <= self.fund:
            self.fund -= amt

    def addFund(self, amt):
        self.fund += amt

    def getFund(self):
        return self.fund
    def getHand(self):
        return self.hand

    def getName(self):
        return self.name
