import random
kind    = ["harten", "klaveren", "schoppen", "ruiten"]
numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "boer", "vrouw", "heer", "aas"]

#Genarate card deck
def Deck():
    deck = []
    for color in range(0, 4):
        selectColor = kind[color]
        for number in range(0, 13):
            selectNumber = numbers[number]
            deck.append(selectColor + " " + selectNumber)
    for j in range(0,2):
        deck.append("joker")
    return deck

def first7(cardlist):
    for pos in range(0,7):
        y = pos + 1
        print("Kaart " + str(y) + ": " + cardlist[pos])

cards = Deck()
random.shuffle(cards)
first7(cards)
print("")
print("deck (47 kaarten): " + str(cards[7:55]))