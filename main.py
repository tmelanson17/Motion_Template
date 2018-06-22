import cv2
import time
from OpenPose.OpenPosePredict import *

ShoulderR = 1
ShoulderL = 2
ArmR = 3
ArmL = 4
WristR = 5
WristL = 6
HipR = 7
HipL = 8
ThighR = 9
ThighL = 10
KneeR = 11
KneeL = 12
LegR = 13 
LegL = 14
FootR = 15
FootL = 16

frame = cv2.imread('OpenPose/single.jpeg')
t = time.time()
points = predict(frame)
angles = create_angles(points)
print("Total time taken : {:.3f}".format(time.time() - t))
print("Angles:")
print(angles)

