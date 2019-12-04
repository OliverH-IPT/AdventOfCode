
#part 1
def checkOpcode(num):
    if num == 1:
        return 'add'
    elif num == 2:
        return 'multiply'
    elif num == 99:
        return 'abort'
    else:
        return 'error'

def saveExit(message):
    print(message)
    exit()

# executes instruction and returns next index
def executeInstruction(intCodeProgram, index, opcode):
    if opcode == 'add' or opcode == 'multiply':
        if index+3 >= len(intCodeProgram):
            saveExit("Index out of bounds in add/multiply instruction")
        # get numbers and indices
        num1 = intCodeProgram[intCodeProgram[index+1]]
        num2 = intCodeProgram[intCodeProgram[index+2]]
        targetIndex = intCodeProgram[index+3]
        if opcode == 'add':
            intCodeProgram[targetIndex] = num1 + num2
        else:
            intCodeProgram[targetIndex] = num1 * num2

        return True, 4

    saveExit("Unknown opcode while executing instruction")

def executeIntCode(intCodeProgram, noun=12, verb=2):

    if(len(intCodeProgram) < 3):
        saveExit("intCodeProgram empty")

    # set noun and verb:
    intCodeProgram[1] = noun
    intCodeProgram[2] = verb

    # Check first opcode
    index = 0
    opcode = checkOpcode(intCodeProgram[index])

    # loop through code 
    while opcode != 'error' and opcode != 'abort':
        # execute instruction and move index
        success, indexIncrement = executeInstruction(intCodeProgram, index, opcode)
        if success != True:
            opcode = 'error'
            break

        index+=indexIncrement
        # check next opcode
        if(len(intCodeProgram) <= index):
            saveExit("Index out of bounds when checking opcode")

        opcode = checkOpcode(intCodeProgram[index])

    if(opcode == 'abort'):
        return True
    else:
        return False

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
