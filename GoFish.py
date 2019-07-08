import random
def main():
    values = list(range(2,11))
    values.append('Jack','Queen','King','Ace')
    suits = ["Spades", "Diamonds", "Hearts", "Clubs"]
    deck = []
    for i in suits:
        for j in values:
            deck.append(Card(i,j))
    random.shuffle(deck)
    AIHand = []
    playerHand = []
    # Deal each player seven cards
    for i in range(7):
        AIHand.append(deck.pop())
        playerHand.append(deck.pop())
    for i in AIHand:
        print(i.toString())
    for j in playerHand:
        print(j.toString())
class Card:
    suit = ""
    value = 0
    def __init__(self, type, val):
        self.suit = type
        self.value = val
    def toString(self):
        return self.value + " of " + self.suit
if __name__ == "__main__":
    main()