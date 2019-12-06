
from days.misc.ErrorHelper import saveExit

def getParam(intCodeProgram, index):
    if index+1 >= len(intCodeProgram):
        saveExit("Index out of bounds in 1 parameters instruction")
    # get numbers and indices
    return intCodeProgram[index+1]

def getParams(intCodeProgram, index, amnt):
    if index+amnt >= len(intCodeProgram):
        saveExit("Index out of bounds in", amnt, "parameters instruction")
    # get numbers and indices
    return intCodeProgram[index+1:index+amnt+1]

def getParamValue(intCodeProgram, param, mode=0):
    return param if mode == 1 else intCodeProgram[param]

def handleAddition(intCodeProgram, modes, index):
    params = getParams(intCodeProgram, index, 3)
    param1 = getParamValue(intCodeProgram, params[0], modes[0])
    param2 = getParamValue(intCodeProgram, params[1], modes[1])
    targetIndex = params[2]
    
    intCodeProgram[targetIndex] = param1 + param2
    
    return True, index+4

def handleMultiplication(intCodeProgram, modes, index):
    params = getParams(intCodeProgram, index, 3)
    param1 = getParamValue(intCodeProgram, params[0], modes[0])
    param2 = getParamValue(intCodeProgram, params[1], modes[1])
    targetIndex = params[2]
    
    intCodeProgram[targetIndex] = param1 * param2
    return True, index+4

def handleInput(intCodeProgram, modes, index):
    targetIndex = getParam(intCodeProgram, index)

    print("Please Input Data:")
    intCodeProgram[targetIndex] = int(input())
    print("Thank you!")
    
    return True, index+2

def handleOutput(intCodeProgram, modes, index):
    param = getParam(intCodeProgram, index)
    output = param if modes[0]==1 else intCodeProgram[param]
    print("Beep Bop, diagnostic test output at index", index, "is:", output)
    return True, index+2

def handleJumpIfTrue(intCodeProgram, modes, index):
    params = getParams(intCodeProgram, index, 2)
    param1 = getParamValue(intCodeProgram, params[0], modes[0])
    param2 = getParamValue(intCodeProgram, params[1], modes[1])
    if param1 != 0:
        return True, param2
    return True, index+3

def handleJumpIfFalse(intCodeProgram, modes, index):
    params = getParams(intCodeProgram, index, 2)
    param1 = getParamValue(intCodeProgram, params[0], modes[0])
    param2 = getParamValue(intCodeProgram, params[1], modes[1])
    if param1 == 0:
        return True, param2
    return True, index+3

def handleLessThan(intCodeProgram, modes, index):
    params = getParams(intCodeProgram, index, 3)
    param1 = getParamValue(intCodeProgram, params[0], modes[0])
    param2 = getParamValue(intCodeProgram, params[1], modes[1])
    targetIndex = params[2]
    if param1 < param2:
        intCodeProgram[targetIndex] = 1
    else:
        intCodeProgram[targetIndex] = 0   
    return True, index+4

def handleEquals(intCodeProgram, modes, index):
    params = getParams(intCodeProgram, index, 3)
    param1 = getParamValue(intCodeProgram, params[0], modes[0])
    param2 = getParamValue(intCodeProgram, params[1], modes[1])
    targetIndex = params[2]
    if param1 == param2:
        intCodeProgram[targetIndex] = 1
    else:
        intCodeProgram[targetIndex] = 0   
    return True, index+4

        
# executes instruction and returns next index
def executeInstruction(intCodeProgram, index, opcode, modes=[0,0,0]):
    if opcode == 'add':
        return handleAddition(intCodeProgram, modes, index)
    if opcode == 'multiply':
        return handleMultiplication(intCodeProgram, modes, index)
    if opcode == 'input':
        return handleInput(intCodeProgram, modes, index)
    if opcode == 'output':
        return handleOutput(intCodeProgram, modes, index)
    if opcode == 'jumpIfTrue':
        return handleJumpIfTrue(intCodeProgram, modes, index)
    if opcode == 'jumpIfFalse':
        return handleJumpIfFalse(intCodeProgram, modes, index)
    if opcode == 'lessThan':
        return handleLessThan(intCodeProgram, modes, index)
    if opcode == 'equals':
        return handleEquals(intCodeProgram, modes, index)

    saveExit("Unknown opcode while executing instruction")