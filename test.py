import cv2
import time
from OpenPose.OpenPosePredict import *
from OpenPose.OpenPoseDraw import drawSkeleton
from serial import Serial
from util import anglesToCommands
from glob import glob
import os


if __name__ == "__main__":
    correct=0
    incorrect=0
    t = time.time()
    pose_directory = "SamplePoses/Homemade_poses/"
    pose_outdir = "output/" + pose_directory
    if not os.path.exists(pose_outdir):
        os.makedirs(pose_outdir)

    for image_file in glob(os.path.join(pose_directory, "*.jpg")):
        frame = cv2.imread(image_file)
        if frame is None:
            raise IOError(image_file + " could not be found")
        # Draw and display skeleton
        points = predictPoints(frame)
        img = drawSkeleton(points, frame)

        cv2.imwrite(os.path.join(pose_outdir, image_file), img) 
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
    print("Total time taken : {:.3f}".format(time.time() - t))
    print("Number correct: {:d}".format(correct))
    print("Number incorrect: {:d}".format(incorrect))
