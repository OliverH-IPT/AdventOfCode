def getDigitList(num):
    return list(map(int,str(num)))

    # Converting integer list to integer...
def convertDigitListToInt(digitList):
    stringList = [str(i) for i in digitList] 
    return int("".join(stringList)) 