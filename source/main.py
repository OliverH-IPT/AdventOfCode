# day 1
import os
from misc.FileHandler import getFileContentByLineAsDbl

from day1.day1 import getFuelRequirements
from day1.day1 import calculateModuleFuelRequirement
from day1.day1 import calculateModuleFuelRequirementRecursively

def Day1_f():
    # part 1
    fileDir = os.path.dirname(__file__)
    relativePath = "../input/day1/input.txt"
    absFilePath = os.path.join(fileDir, relativePath)
    inputMasses = getFileContentByLineAsDbl(absFilePath)

    requiredFuel = getFuelRequirements(inputMasses, calculateModuleFuelRequirement)
    print("Required Fuel:", requiredFuel)

    # part 2
    # for some reason i cannot use 'inputMasses' a second time...
    inputMasses2 = getFileContentByLineAsDbl(absFilePath)
    requiredFuel2 = getFuelRequirements(inputMasses2, calculateModuleFuelRequirementRecursively)
    print("Required Fuel (recursive):", requiredFuel2)

#Day1_f()

# day 2
import copy
from misc.FileHandler import getFileContentByCommaSeperation
from day2.day2 import executeIntCode
from day2.day2 import findNounAndVerb, executeIntCodeCopy
def Day2_f():
    fileDir = os.path.dirname(__file__)
    relativePath = "../input/day2/input.txt"
    absFilePath = os.path.join(fileDir, relativePath)
    intcodeProgram = getFileContentByCommaSeperation(absFilePath)
    
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
    print("noun = ", noun, "verb = ", verb, "result in output = ", executeIntCodeCopy(intcodeProgram, noun, verb))
    print("Result = ", 100 * noun + verb)

Day2_f()