import cv2
import time
import numpy as np
import os 

MODE = "MPI"
pose_directory =  os.path.dirname(__file__)
if MODE is "COCO":
    protoFile = os.path.join(pose_directory, "pose/coco/pose_deploy_linevec.prototxt")
    weightsFile = os.path.join(pose_directory, "pose/coco/pose_iter_440000.caffemodel")
    nPoints = 18
    POSE_PAIRS = [ [1,0],[1,2],[1,5],[2,3],[3,4],[5,6],[6,7],[1,8],[8,9],[9,10],[1,11],[11,12],[12,13],[0,14],[0,15],[14,16],[15,17]]
 
elif MODE is "MPI" :
    protoFile = os.path.join(pose_directory, "pose/mpi/pose_deploy_linevec_faster_4_stages.prototxt")
    weightsFile = os.path.join(pose_directory, "pose/mpi/pose_iter_160000.caffemodel")
    nPoints = 15
    POSE_PAIRS = [[0,1], [1,2], [2,3], [3,4], [1,5], [5,6], [6,7], [1,14], [14,8], [8,9], [9,10], [14,11], [11,12], [12,13] ]
    POSE_REF = { "ShoulderR": [5, 2, 3], "ArmR": [2, 3, 4], "ShoulderL": [2, 5, 6], "ArmL": [5,6,7]}
 
# Returns: A list of points in a certain order
def predict(frame):
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
 
# Returns: angles from the set of points, dependent on model type
def create_angles(points):
    angles = dict()
    for joint_name in POSE_REF:
        refs = POSE_REF[joint_name]
        inner = refs[0]
        mid = refs[1]
        outer = refs[2]
        if points[inner] and points[mid] and points[outer]:
            link1 = np.array(points[inner]) - np.array(points[mid])
            link2 = np.array(points[outer]) - np.array(points[mid])
            cosine = np.dot(link1, link2) / (np.linalg.norm(link1) * np.linalg.norm(link2))
            angle = np.arccos(cosine)
            angles[joint_name] = angle
    return angles
 
if __name__ == "__main__": 
    frame = cv2.imread('single.jpeg')
    t = time.time()
    points = predict(frame)
    angles = create_angles(points)
    print("Total time taken : {:.3f}".format(time.time() - t))
    print("Angles:")
    print(angles)
