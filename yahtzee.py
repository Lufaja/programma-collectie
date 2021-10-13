import random
diceNumbers = ['1', '2', '3', '4', '5', '6']
stored = []
rollTimes = 0
vari = True
small1 = ["1", "2", "3", "4"]
small2 = ["2", "3", "4", "5"]
small3 = ["3", "4", "5", "6"]
big1   = ["1", "2", "3", "4", "5"]
big2   = ["2", "3", "4", "5", "6"]

scoreDic = {
    "aces" : 0,
    "twos" : 0,
    "threes" : 0,
    "fours" : 0,
    "fives" : 0,
    "sixes" : 0,
    "three of a kind" : 0,
    "four of a kind" : 0,
    "full house" : 0,
    "small straight" : 0,
    "large straight" : 0,
    "yahtzee" : 0,
    "chance" : 0,
    "total points" : 0,
    "total points 1" : 0,
    "total points 2" : 0
}

def roll(keptDice:list):
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
def keepDice(rollDice:list, keptDice:list):
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

def calculate(dice:list):
    if "1" in dice and scoreDic.get("aces") == 0:
        var1 = dice.count("1")
        print("aces           : ", var1*1)
    if "2" in dice and scoreDic.get("twos") == 0:
        var2 = dice.count("2")
        print("twos           : ", var2*2)
    if "3" in dice and scoreDic.get("threes") == 0:
        var3 = dice.count("3")
        print("threes         : ", var3*3)
    if "4" in dice and scoreDic.get("fours") == 0:
        var4 = dice.count("4")
        print("fours          : ", var4*4)
    if "5" in dice and scoreDic.get("fives") == 0:
        var5 = dice.count("5")
        print("fives          : ", var5*5)
    if "6" in dice and scoreDic.get("sixes") == 0:
        var6 = dice.count("6")
        print("sixes          : ", var6*6)
    if threeKind(dice, 1) == True and scoreDic.get("three of a kind") == 0:
        print("three of a kind: ", threeKind(dice,0))
    if fourKind(dice, 1) == True and scoreDic.get("four of a kind") == 0:
        print("four  of a kind: ", fourKind(dice,0))
    if fullHouse(dice) == True and scoreDic.get("full house") == 0:
        print("full house     :  25")
    if smallStraight(dice) == True and scoreDic.get("small straight") == 0:
        print("small straight :  30")
    if bigStraight(dice) == True and scoreDic.get("large straight") == 0:
        print("large straight :  40")
    if yahtzee(dice) == True and scoreDic.get("yahtzee") == 0:
        print("yahtzee        :  50")
    if yahtzee(dice) == True and scoreDic.get("yahtzee") != 0:
        print("extra yahtzee  :  100")
    if scoreDic.get("chance") == 0:
        print("chance         : ", (int(dice[0])+int(dice[1])+int(dice[2])+int(dice[3])+int(dice[4])))


def threeKind(dice:list, version):
    for z in range(1, 7):
        count_ = dice.count(str(z))
        if count_ == 3 and version == 0:
            return (int(dice[0])+int(dice[1])+int(dice[2])+int(dice[3])+int(dice[4]))
        elif count_ == 3 and version == 1:
            return True
    return False

def fourKind(dice:list, version):
    for z in range(1, 7):
        count_ = dice.count(str(z))
        if count_ == 4 and version == 0:
            return (dice[0]+dice[1]+dice[2]+dice[3]+dice[4])
        elif count_ == 4 and version == 1:
            return True
    return False

def fullHouse(dice:list):
    for z in range(1, 7):
        count_ = dice.count(str(z))
        if count_ == 3:
            for z in range(1, 7):
                count_ = dice.count(str(z))
                if count_ == 2:
                    return True
    return False

def smallStraight(dice:list):
    if all(elem in dice for elem in small1) == True:
        return True
    if all(elem in dice for elem in small2) == True:
        return True
    if all(elem in dice for elem in small3) == True:
        return True
    return False

def bigStraight(dice:list):
    if all(elem in dice for elem in big1) == True:
        return True
    if all(elem in dice for elem in big2) == True:
        return True    
    return False

def yahtzee(dice:list):
    for x in range(1, 7):
        count_ = dice.count(str(x))
        if count_ == 5:
            return True
    return False

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