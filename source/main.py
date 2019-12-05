# day 1
import os, copy
from misc.FileHandler import getFileContentByLine, convertToFloatMap

from days.day1 import getFuelRequirements
from days.day1 import calculateModuleFuelRequirement
from days.day1 import calculateModuleFuelRequirementRecursively

def Day1_f():
    # part 1
    fileDir = os.path.dirname(__file__)
    relativePath = "../input/day1/input.txt"
    absFilePath = os.path.join(fileDir, relativePath)
    inputMasses = convertToFloatMap(getFileContentByLine(absFilePath))

    requiredFuel = getFuelRequirements(copy.deepcopy(inputMasses), calculateModuleFuelRequirement)
    print("Required Fuel:", requiredFuel)

    # part 2
    # for some reason i cannot use 'inputMasses' a second time...
    requiredFuel2 = getFuelRequirements(inputMasses, calculateModuleFuelRequirementRecursively)
    print("Required Fuel (recursive):", requiredFuel2)

Day1_f()

# day 2
from misc.FileHandler import getFileContentByCommaSeperation, convertToNumberList
from days.day2 import executeIntCode
from days.day2 import findNounAndVerb, executeIntCodeCopy
def Day2_f():
    fileDir = os.path.dirname(__file__)
    relativePath = "../input/day2/input.txt"
    absFilePath = os.path.join(fileDir, relativePath)
    intcodeProgram = convertToNumberList(getFileContentByCommaSeperation(absFilePath))
    
    # part 1
    print("-------- Part 1 -----------")
    intcodeProgramCopy = copy.deepcopy(intcodeProgram)
    if executeIntCode(intcodeProgramCopy) == True:
        print("Successfully ran default intcode program")
        print("Result: ", intcodeProgramCopy[0])
    else:
        print("Error while running intcode program")

    # part 2
    print("-------- Part 2 -----------")
    noun, verb = findNounAndVerb(intcodeProgram)
    print("noun = ", noun, ", verb = ", verb, ", result in output = ", executeIntCodeCopy(intcodeProgram, noun, verb))
    print("Result = ", 100 * noun + verb)

#Day2_f()

# day 3
from days.day3 import getNearestIntersection, getMinimumSignalDistance
def Day3_f():
    fileDir = os.path.dirname(__file__)
    relativePath = "../input/day3/input.txt"
    absFilePath = os.path.join(fileDir, relativePath)

    wires = []
    for wire in getFileContentByLine(absFilePath):
        wires.append(wire.split(','))

    #part 1
    # point = getNearestIntersection(wires)
    # print("Nearest intersection by Manhattan distance is at", point, " having a distance of", point.distance)

    #part 2
    minDist, intersection = getMinimumSignalDistance(wires)
    print("Nearest intersection by signal distance is at", intersection, " having a distance of", minDist)
#Day3_f()

from days.day4 import getNumberOfPasswords, checkPassword, checkPassword_part2
def Day4_f():
    #part 1
    pwCount = getNumberOfPasswords(checkPassword)
    print("Total amount of possible passwords for part 1 is", pwCount)

    #part 2
    pwCount2 = getNumberOfPasswords(checkPassword_part2)
    print("Total amount of possible passwords for part 2 is", pwCount2)
#Day4_f()