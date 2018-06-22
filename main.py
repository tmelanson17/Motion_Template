import cv2
import time
from OpenPose.OpenPosePredict import *
from serial import Serial


radToDegree = lambda f: 180 * f / 3.14159 

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

serialName="" # TODO: Fill in the proper name for the serial output

ser = Serial
frame = cv2.imread('OpenPose/single.jpeg')
t = time.time()
points = predict(frame)
angles = create_angles(points)
for key in angles:
   outputStr = "M%02d%03d" % (motorNames[key], radToDegree(angles[key]))
   print(outputStr)
   # TODO: Output this to serial

print("Total time taken : {:.3f}".format(time.time() - t))
