from card import Card
class Player:
    def __init__(self, name, fund, dealer=False):
        self.name = name
        self.fund = fund
        self.hand = []
        self.dealer = dealer
        self.bet = 5

    def bust(self)->bool:
        return False
    def action(self)->str:
        #hit and stand for now

        return "hit"
    def receiveCard(self, card: Card):
        self.hand.append(card)

    def report(self):
        print(self.name, self.fund, self.hit, [card.getCard() for card in self.hand])

    def handValue(self):
        val = set()

        for c in self.hand:
            if c.num is not "A":
                if not self.hand:
                    val.add(c.num)
                else:
                    for v in val:
                        val.add(val.pop(v) + c.num)
            else: #It's ACE
                if not self.hand:
                    val.add(1)
                    val.add(11)
                else:
                    for v in val:
                        val.pop(v)
                        val.add(v + 1)
                        if v + 11 <= 21:
                            val.add(v + 11)



        return val



    def modifyFund(self, amount):
        self.fund += amount
