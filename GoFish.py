import random
def main():
    values = list(str(range(2,11)))
    values.extend(['Jack','Queen','King','Ace'])
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
    # for i in AIHand:
    #     print(i.toString())
    # for j in playerHand:
    #     print(j.toString())
    AIBooks = 0
    playerBooks = 0
    playerTurn = True
    #TODO removeBooks and case of hands running out of cards
    while len(deck) > 0 or len(playerHand) > 0 or len(AIHand) > 0:
        if playerTurn:
            while True:
                print(f"You have the cards {playerHand}")
                askFor = input("What do you want to ask for")
                if askFor in values:
                    for i in playerHand:
                        if i.value == askFor:
                            break
                        else:
                            print("Error: You must have at least on of those cards")
                else:
                    print(f"Error: Input must be one of {values}")
            takeCards = theyHave(AIHand, askFor)
            if len(takeCards) > 0:
                print(f"You got {len(takeCards)} cards")
                takeCards.reverse
                for i in takeCards:
                    playerHand.append(AIHand.pop(i))
            else:
                print("Go fish")
                goFishCard = deck.pop()
                playerHand.append(goFishCard)
                if goFishCard.value != askFor:
                    playerTurn = False
                    print("You didn't get what you asked for")
                else:
                    print(f"You got a {goFishCard.value} which is what you asked for")
        else:
            AIIndex = random.uniform(0,len(AIHand))
            askFor = AIHand[AIIndex].value
            print(f"The computer asked for {askFor}")
            takeCards = theyHave(playerHand, askFor)
            if len(takeCards) > 0:
                print(f"The computer got {len(takeCards)} cards")
                takeCards.reverse
                for i in takeCards:
                    AIHand.append(playerHand.pop(i))
            else:
                print("Go fish")
                goFishCard = deck.pop()
                AIHand.append(goFishCard)
                if goFishCard.value != askFor:
                    playerTurn = True
                    print("The computer didn't get what it asked for")
def removeBook(hand, cardValue):
    locations = []
    index = 0
    for i in hand:
        if i.value == cardValue:
            locations.append(index)
        index += 1
    if len(locations) == 4:
        locations.reverse
        for i in locations:
            locations.remove(i)
        return 1
    return 0
def theyHave(theirHand, asked):
    indices = []
    index = 0
    for i in theirHand:
        if i.value == asked:
            indices.append(index)
        index += 1
    return indices
class Card:
    suit = ""
    value = ''
    def __init__(self, type, val):
        self.suit = type
        self.value = val
    def toString(self):
        return self.value + " of " + self.suit
if __name__ == "__main__":
    main()