def convertToFloatMap(stringList):
    return map(float, stringList)
    
def convertToNumberList(stringList):
    return list(map(int, stringList))
    
def convertToOrbits(stringList):
    orbitPairs =[]
    for string in stringList:
        orbitPairs.append(string.split(')'))

    return orbitPairs