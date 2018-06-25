import cv2
import time
import numpy as np
import os 
from OpenPose.OpenPoseUtil import *

# Returns: A list of points in a certain order
def predictPoints(frame):
    frameCopy = np.copy(frame)
    frameWidth = frame.shape[1]
    frameHeight = frame.shape[0]
    threshold = 0.1
 
    net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)
 
    t = time.time()
    # input image dimensions for the network
    inWidth = 368
    inHeight = 368
    inpBlob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (inWidth, inHeight),
                  (0, 0, 0), swapRB=False, crop=False)
 
    net.setInput(inpBlob)
 
    output = net.forward()
    print("time taken by network : {:.3f}".format(time.time() - t))
 
    H = output.shape[2]
    W = output.shape[3]
 
    # Empty list to store the detected keypoints
    points = []
 
    for i in range(nPoints):
        # confidence map of corresponding body's part.
        probMap = output[0, i, :, :]
 
        # Find global maxima of the probMap.
        minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)
        
        # Scale the point to fit on the original image
        x = (frameWidth * point[0]) / W
        y = (frameHeight * point[1]) / H
 
        if prob > threshold : 
            # Add the point to the list if the probability is greater than the threshold
            points.append((int(x), int(y)))
        else :
            points.append(None)
    return points
 

# Returns: True if the output is complete, False otherwise
def fully_formed_output(angles):
    return len(angles) == len(POSE_REF) 


# Returns: angles from the set of points, dependent on model type
def create_angles(points):
    angles = dict()
    for joint_name in POSE_REF:
        # Get reference points for the angle
        refs = POSE_REF[joint_name]
        inner = refs[0]
        mid = refs[1]
        outer = refs[2]
        if points[inner] and points[mid] and points[outer]:
            link1 = np.array(points[inner]) - np.array(points[mid])
            link2 = np.array(points[outer]) - np.array(points[mid])
            if np.any(np.isnan(link1)) or np.any(np.isnan(link2)):
                continue
            # Find the angle between link1 and link2 using dot product
            cosine = np.dot(link1, link2) / (np.linalg.norm(link1) * np.linalg.norm(link2))
            angle = np.arccos(cosine)
            angles[joint_name] = angle
    return fully_formed_output(angles), angles


# Returns: The set of angles
def predictAngles(frame):
    points = predictPoints(frame)
    formed, angles = create_angles(points)
    if not formed:
        return None
    return formed, angles


if __name__ == "__main__": 
    frame = cv2.imread('single.jpeg')
    t = time.time()
    points = predict(frame)
    angles = create_angles(points)
    print("Total time taken : {:.3f}".format(time.time() - t))
    print("Angles:")
    print(angles)
