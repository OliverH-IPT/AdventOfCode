#part1

def getInputRange():
    return 145852, 616942

def hasOneEqualAdjacent(digitList):
    iterDigitList = iter(digitList)
    d1 = next(iterDigitList)

    for d2 in iterDigitList:
        if d1 == d2:
            return True
        d1 = d2
    return False

def checkPassword(digitList):
    iterDigitList = iter(digitList)
    d1 = next(iterDigitList)
    oneEqual = False
    failedDigitIndex = 0
    for d2 in iterDigitList:
        if d1 == d2:
            oneEqual = True
        if d1 > d2:
            return False, failedDigitIndex
        d1 = d2
        failedDigitIndex+=1

    return oneEqual, -1

from days.misc.DigitHelper import convertDigitListToInt
def getNextPossibleNumber(digitList, failedDigitIndex):
    pivotDigit = digitList[failedDigitIndex]
    for i in range(failedDigitIndex+1, len(digitList)):
        digitList[i] = pivotDigit
    
    return convertDigitListToInt(digitList)

from days.misc.DigitHelper import getDigitList
def getNumberOfPasswords(passwordChecker):
    min, max = getInputRange()

    num = 0
    i = min
    while i <= max:
        digitList = getDigitList(i)
        isValid, failedDigitIndex = passwordChecker(digitList)
        if isValid == True:
            num+=1
            #print("valid =", i)
            i+=1
        else:
            if failedDigitIndex == -1: #too many or too few adjacents
                i+=1
            else: #decreasing digit
                i = getNextPossibleNumber(digitList, failedDigitIndex)
            #print("next possible =", i)
    return num

#part 2
def checkPassword_part2(digitList):
    iterDigitList = iter(digitList)
    d1 = next(iterDigitList)
    oneEqual = False
    failedDigitIndex = 0
    numEquals = 0
    for d2 in iterDigitList:
        if d1 > d2: # violated increment rule
            return False, failedDigitIndex   
        elif d1 == d2: # equal digit => counter up
            numEquals+=1
        else: # d1 < d2
            if numEquals == 1: # if last two digits were equal, this might be valid pw
                oneEqual = True
            numEquals = 0

        d1 = d2 #update ref
        failedDigitIndex+=1

    if numEquals == 1: # last two digits could be equal
        oneEqual = True

    return oneEqual, -1