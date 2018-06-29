import numpy as np
from serial import Serial

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

serialName="/dev/tty.Bluetooth-Incoming-Port" # TODO: Fill in the proper name for the serial output
ser = Serial(serialName,9600)


def anglesToCommands(angles):
    outputCommands = list()
    for key in angles:
       outputStr = "M%02d%03d" % (motorNames[key], radToDegree(angles[key]))
       # print(outputStr)
       outputCommands.append(outputStr)
    return outputCommands


