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
    while len(deck) > 0:
        if playerTurn:
            while true:
                print(f"You have the cards {playerHand}")
                askFor = input("What do you want to ask for")
                if askfor in values:
                    for i in playerHand:
                        if i.value == askFor:
                            break
                        else:
                            print("Error: You must have at least on of those cards")
                else:
                    print(f"Error: Input must be one of {values}")
            
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