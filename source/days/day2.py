
#part 1
from days.misc.DigitHelper import getDigitList, convertDigitListToInt
def checkOpcode(num):
    dl = getDigitList(num)
    modes = [0, 0, 0]

    opcode = convertDigitListToInt(dl[-2:])

    modeList = dl[:-2]
    i = 0
    for mode in reversed(modeList):
        modes[i] = mode
        i+=1
    

    if opcode == 1:
        return 'add', modes
    elif opcode == 2:
        return 'multiply', modes
    elif opcode == 3:
        return 'input', modes
    elif opcode == 4:
        return 'output', modes
    elif opcode == 99:
        return 'abort', modes
    else:
        return 'error', modes

# dl = getDigitList(num)
#     opcode = convertDigitListToInt(dl[-2:])
#     print(opcode)

from days.misc.ErrorHelper import saveExit
# executes instruction and returns next index
def executeInstruction(intCodeProgram, index, opcode, modes=[0,0,0]):

    if opcode == 'add' or opcode == 'multiply':
        if index+3 >= len(intCodeProgram):
            saveExit("Index out of bounds in add/multiply instruction")
        # get numbers and indices
        params = intCodeProgram[index+1:index+4]
        num1 = params[0] if modes[0] == 1 else intCodeProgram[params[0]]
        num2 = params[1] if modes[1] == 1 else intCodeProgram[params[1]]
        targetIndex = params[2]
        if opcode == 'add':
            intCodeProgram[targetIndex] = num1 + num2
        else:
            intCodeProgram[targetIndex] = num1 * num2
        return True, 4

    if opcode == 'input':
        if index+1 >= len(intCodeProgram):
            saveExit("Index out of bounds in input instruction")

        print("Please Input Data: 1 thank you")
        targetIndex = intCodeProgram[index+1]
        intCodeProgram[targetIndex] = 1
        #int(input())
        return True, 2

    if opcode == 'output':
        param = intCodeProgram[index+1]
        output = param if modes[0]==1 else intCodeProgram[param]
        print("Beep Bop, diagnostic test output at index", index, "is:", output)
        return True, 2

    saveExit("Unknown opcode while executing instruction")

def executeUnchangedIntCode(intCodeProgram):
     # Check first opcode
    index = 0
    opcode, modes = checkOpcode(intCodeProgram[index])

    # loop through code 
    while opcode != 'error' and opcode != 'abort':
        # execute instruction and move index
        success, indexIncrement = executeInstruction(intCodeProgram, index, opcode, modes)
        if success != True:
            opcode = 'error'
            break
        index+=indexIncrement

        # check next opcode
        if(len(intCodeProgram) <= index):
            saveExit("Index out of bounds when checking opcode")
        opcode, modes = checkOpcode(intCodeProgram[index])

    if(opcode == 'abort'):
        return True
    else:
        return False

def executeIntCode(intCodeProgram, noun=12, verb=2):

    if(len(intCodeProgram) < 3):
        saveExit("intCodeProgram empty")

    # set noun and verb:
    intCodeProgram[1] = noun
    intCodeProgram[2] = verb

    return executeUnchangedIntCode(intCodeProgram)

#part 2
import copy
def executeIntCodeCopy(intCodeProgram, noun=12, verb=2):
    memory = copy.deepcopy(intCodeProgram)
    if(executeIntCode(memory, noun, verb)):
        return memory[0]
    else:
        print("Error while running intcode program with noun = ", noun, ", verb = ", verb)
        return -1

def findNounAndVerb(intCodeProgram, target = 19690720):
    noun = binarySearchNoun(intCodeProgram, target, 0)
    verb = binarySearchVerb(intCodeProgram, target, noun)
    return noun, verb

import math
def binarySearchNoun(intCodeProgram, target, verb, L=0, H=99):
    while (H-L > 1):
        noun = math.floor((H+L)/2)
        if executeIntCodeCopy(intCodeProgram, noun, verb) > target:
            H = noun
        else:
            L = noun
    return L
    
def binarySearchVerb(intCodeProgram, target, noun, L=0, H=99):
    while (H-L > 1):
        verb = math.floor((H+L)/2)
        if executeIntCodeCopy(intCodeProgram, noun, verb) > target:
            H = verb
        else:
            L = verb
    return L
