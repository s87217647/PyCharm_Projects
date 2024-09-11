import random
from card import Card
class Deck:
    def __init__(self, numOfDecks):
        self.stack = []
        self.initialize(numOfDecks)

    def initialize(self, num):
        for x in range(num):
            self.stack.extend(self.oneDeck())

        random.shuffle(self.stack)
        return self.stack

    def pop(self):
        return self.stack.pop()



    def clear(self):
        return


    def printDeck(self):
        print("Size of the deck is: ", len(self.stack))
        for card in self.stack:
            print(card.getCard())



    #Note that Jokers are excluded
    def oneDeck(self):
        res = []
        nums = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        suits = ['D', 'C', 'H', 'S']

        for num in nums:
            for suit in suits:
                res.append(Card(num, suit))

        return res


