import random
diceNumbers = ['1', '2', '3', '4', '5', '6']
stored = []
rollTimes = 0
vari = True

def roll(keptDice):
    global rollTimes
    rollTimes += 1
    diceAmount = 5 - len(keptDice)
    rollDice = []
    for x in range(0, diceAmount):
        rollDice.append(random.choice(diceNumbers))
    print("You rolled: " + str(rollDice))
    print("Stored dice: " + str(keptDice))
    if rollTimes < 3:
        keptDices = keepDice(rollDice, keptDice)
    alldice = rollDice + keptDice
    calculate(alldice)
    if rollTimes < 3:
        choice(keptDices)
    elif rollTimes == 3:
        #iets met scoren
        pass
        
def choice(keptDice):
    ans = input("Roll or Score?: ").lower()
    if ans == "roll":
        roll(keptDice)
    elif ans == "score":
        pass
    else:
        choice(keptDice)

#choice for keeping dice from roll or putting them back
def keepDice(rollDice, keptDice):
    while len(keptDice) <= 5:
        rdice = rollDice.copy()
        kdice = keptDice.copy()
        ans1 = input("Keep or Return: ").lower()
        splitAns = ans1.split()
        if splitAns[0] == "stop":
            break
        if splitAns[0] != "keep" and splitAns[0] != "return":
            print("Type stop to exit")
            continue
        splitAns.pop(0)
        sP1 = splitAns.copy()
        sP2 = splitAns.copy()
        if keep(rdice, sP1) == True and "keep" in ans1:
            for y in range(0,len(splitAns)):
                keptDice.append(splitAns[y])
                rollDice.remove(splitAns[y])
        elif returN(kdice, sP2) == True and "return" in ans1:
            for y in range(0,len(splitAns)):
                keptDice.remove(splitAns[y])
                rollDice.append(splitAns[y])
        else:
            print("Type stop to exit")
        print(keptDice)
        print(rollDice)
    return keptDice


def keep(dices, ansKeep):
    if len(ansKeep) > len(dices):
        vari = False
    else:
        for x in range(0, len(ansKeep)):
            vari = all(elem in dices  for elem in ansKeep)
            if vari == False:
                break
            dices.remove(ansKeep[0])
            ansKeep.pop(0)
    return vari

def returN(kepdice, ansKeep):
    if len(ansKeep) > len(kepdice):
        variable = False
    else:
        for x in range(0, len(ansKeep)):
            variable = all(elem in kepdice  for elem in ansKeep)
            if variable == False:
                break
            kepdice.remove(ansKeep[0])
            ansKeep.pop(0)
    return variable


def game():
    input("Press ENTER to start game")

def calculate(dice):
    if "1" in dice:
        var1 = dice.count("1")
        print("aces       : ", var1*1)
    if "2" in dice:
        var2 = dice.count("2")
        print("twos       : ", var2*2)
    if "3" in dice:
        var3 = dice.count("3")
        print("threes     : ", var3*3)
    if "4" in dice:
        var4 = dice.count("4")
        print("fours      : ", var4*4)
    if "5" in dice:
        var5 = dice.count("5")
        print("fives      : ", var5*5)
    if "6" in dice:
        var6 = dice.count("6")
        print("sixes      : ", var6*6)


def scorebord():
    print("-------------------------------------")
    print("|   PART 1   |   SCORE   |   GAME 1  |")
    print("-------------------------------------")
    print("|   ACES    |  TOTAL 1S |   " + str(aces) + "   |")
    print("-------------------------------------")
    print("|   TWOS    |  TOTAL 2S |   " + str(twos) + "  |")
    print("-------------------------------------")
    print("|   THREES  |  TOTAL 3S |   " + str(threes) + "  |")
    print("-------------------------------------")
    print("|   FOURS   |  TOTAL 4S |   " + str(fours) + "  |")
    print("-------------------------------------")
    print("|   FIVES   |  TOTAL 5S |   " + str(fives) + "  |")
    print("-------------------------------------")
    print("|   SIXES   |  TOTAL 6S |   " + str(sixes) + "  |")
    print("-------------------------------------")
    print("|   TOTAL POINST ------>|   " + str() + "  |")
    print("-------------------------------------")

game()
roll(stored)