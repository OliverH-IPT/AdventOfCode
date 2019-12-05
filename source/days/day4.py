#part1

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


def getNextPossibleNumber(digitList, failedDigitIndex):
    pivotDigit = digitList[failedDigitIndex]
    for i in range(failedDigitIndex+1, len(digitList)):
        digitList[i] = pivotDigit
    
    # Converting integer list to integer...
    stringList = [str(i) for i in digitList] 
    return int("".join(stringList)) 


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
        if d1 == d2:
            numEquals+=1
        elif d1 > d2:
            return False, failedDigitIndex    
        elif numEquals == 1:
            oneEqual = True
            numEquals = 0
        else:
            numEquals = 0

        d1 = d2
        failedDigitIndex+=1

    if numEquals == 1:
        oneEqual = True

    return oneEqual, -1