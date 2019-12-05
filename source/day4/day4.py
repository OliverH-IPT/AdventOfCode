def getInputRange():
    return 145852, 616942

def getDigitList(num):
    return list(map(int,str(num)))

def hasOneEqualAdjacent(digitList):
    iterDigitList = iter(digitList)
    d1 = next(iterDigitList)

    for d2 in iterDigitList:
        if d1 == d2:
            return True
        d1 = d2
    return False

def getNumberOfPasswords():
    min, max = getInputRange()

    totalPwAmnt = max-min+1
    print("Total amnt of pws is", totalPwAmnt)

    maxList = getDigitList(max)


    res = 0
    return hasOneEqualAdjacent(maxList)