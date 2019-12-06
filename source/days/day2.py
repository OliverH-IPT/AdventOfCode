
from days.misc.DigitHelper import getDigitList, convertDigitListToInt
def checkOpcode(num):
    dl = getDigitList(num)
    opcode = convertDigitListToInt(dl[-2:])

    opcodeString = 'error'
    if opcode == 1:
        opcodeString ='add'
    elif opcode == 2:
        opcodeString ='multiply'
    elif opcode == 3:
        opcodeString ='input'
    elif opcode == 4:
        opcodeString ='output'
    elif opcode == 5:
        opcodeString ='jumpIfTrue'
    elif opcode == 6:
        opcodeString ='jumpIfFalse'
    elif opcode == 7:
        opcodeString ='lessThan'
    elif opcode == 8:
        opcodeString ='equals'
    elif opcode == 99:
        opcodeString ='abort'

    modes = [0, 0, 0]
    modeList = dl[:-2]
    i = 0
    for mode in reversed(modeList):
        modes[i] = mode
        i+=1

    return opcodeString, modes

from days.misc.ErrorHelper import saveExit
from days.misc.InstructionHelper import executeInstruction

def executeUnchangedIntCode(intCodeProgram):
     # Check first opcode
    index = 0
    opcode, modes = checkOpcode(intCodeProgram[index])

    # loop through code 
    while opcode != 'error' and opcode != 'abort':
        # execute instruction and move index
        success, index = executeInstruction(intCodeProgram, index, opcode, modes)
        if success != True:
            opcode = 'error'
            break

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
