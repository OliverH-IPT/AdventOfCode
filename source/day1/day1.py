
#part 1

def getFuelRequirements(moduleMasses, calculationMethod):
    requiredFuel = 0
    for mass in moduleMasses:
        requiredFuel += calculationMethod(mass)

    return requiredFuel

import math

def calculateModuleFuelRequirement(mass):
    return math.floor(mass/3)-2

#part 2

def calculateModuleFuelRequirementRecursively(mass):
    # calculate required fuel for current module
    requiredFuel = calculateModuleFuelRequirement(mass)
    if requiredFuel > 0:
        # add additional cost of mass of required fuel
        return requiredFuel + calculateModuleFuelRequirementRecursively(requiredFuel)
    
    return 0