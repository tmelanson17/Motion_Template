from OpenPose.OpenPoseUtil import *
import numpy as np
import cv2

def drawSkeleton(points, frame):    
    frameCopy = np.copy(frame)
    # Draw Skeleton
    for pair in POSE_PAIRS:
        partA = pair[0]
        partB = pair[1]
    
        if points[partA] and points[partB]:
            cv2.line(frameCopy, points[partA], points[partB], (0, 255, 255), 2)
            cv2.circle(frameCopy, points[partA], 8, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)
    
    return frameCopy
