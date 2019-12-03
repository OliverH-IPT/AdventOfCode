# day 1
from misc.FileHandler import getFileContentByLineAsDbl
import os

# part 1
fileDir = os.path.dirname(__file__)
relativePath = "../input/day1/input.txt"
abs_file_path = os.path.join(fileDir, relativePath)
inputMasses = getFileContentByLineAsDbl(abs_file_path)


from day1.day1 import getFuelRequirements
from day1.day1 import calculateModuleFuelRequirement
requiredFuel = getFuelRequirements(inputMasses, calculateModuleFuelRequirement)
print("Required Fuel:", requiredFuel)

# part 2

from day1.day1 import calculateModuleFuelRequirementRecursively
# for some reason i cannot use 'inputMasses' a second time...
inputMasses2 = getFileContentByLineAsDbl(abs_file_path)
requiredFuel2 = getFuelRequirements(inputMasses2, calculateModuleFuelRequirementRecursively)
print("Required Fuel (recursive):", requiredFuel2)