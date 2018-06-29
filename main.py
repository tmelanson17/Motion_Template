import cv2
import time
from OpenPose.OpenPosePredict import *
from serial import Serial
from video_loop import spin
from util import *

if __name__ == "__main__":
    imgFile = 'OpenPose/single.jpeg'
    frame = cv2.imread(imgFile)
    if frame is None:
        raise IOError(imgFile + " could not be found")
    t = time.time()
    formed, angles = predictAngles(frame)
    if formed:
        commands = anglesToCommands(angles)
        for com in commands:
            ser.write(com.encode())
            print(com)
    # spin(lambda f: predictAngles(f))
    print("Total time taken : {:.3f}".format(time.time() - t))
