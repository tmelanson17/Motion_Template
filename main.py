import cv2
import time
from OpenPose.OpenPosePredict import *
from serial import Serial
from video_loop import spin
from util import anglesToCommands

serialName="com4" # TODO: Fill in the proper name for the serial output

if __name__ == "__main__":
    ser = Serial(serialName,9600)
    frame = cv2.imread('SamplePoses/stock_wave.jpg')
    t = time.time()
    formed, angles = predictAngles(frame)
    if formed:
        commands = anglesToCommands(angles)
        for com in commands:
            ser.write(outputStr.encode())
    # spin(lambda f: predictAngles(f))
    print("Total time taken : {:.3f}".format(time.time() - t))
