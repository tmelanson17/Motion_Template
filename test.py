import cv2
import time
from OpenPose.OpenPosePredict import *
from OpenPose.OpenPoseDraw import drawSkeleton
from serial import Serial
from video_loop import spin
from util import anglesToCommands
from glob import glob


if __name__ == "__main__":
    correct=0
    incorrect=0
    t = time.time()
    for image_file in glob("SamplePoses/Homemade_poses/IMG_20180625_09404*.jpg"):
        frame = cv2.imread(image_file)
        # Draw and display skeleton
        points = predictPoints(frame)
        img = drawSkeleton(points, frame)
        cv2.imshow("Pose",img)
        cv2.waitKey(0)
 
        # Check if the pose was detected
        formed, angles = create_angles(points)
        if formed:
            print("Incoming command: ")
            commands = anglesToCommands(angles)
            for com in commands:
                print(com)
            correct+=1
        else:
            incorrect+=1
        # spin(lambda f: predictAngles(f))
    print("Total time taken : {:.3f}".format(time.time() - t))
    print("Number correct: {:d}".format(correct))
    print("Number incorrect: {:d}".format(incorrect))
