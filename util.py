import numpy as np

motorNames = {
"ShoulderR" : 1,
"ShoulderL" : 2,
"ArmR" : 3,
"ArmL" : 4,
"WristR" : 5,
"WristL" : 6,
"HipR" : 7,
"HipL" : 8,
"ThighR" : 9,
"ThighL" : 10,
"KneeR" : 11,
"KneeL" : 12,
"LegR" : 13 ,
"LegL" : 14,
"FootR" : 15,
"FootL" : 16
}


radToDegree = lambda f: 180 * f / 3.14159 

def anglesToCommands(angles):
    outputCommands = list()
    for key in angles:
       outputStr = "M%02d%03d" % (motorNames[key], radToDegree(angles[key]))
       # print(outputStr)
       outputCommands.append(outputStr)
    return outputCommands


