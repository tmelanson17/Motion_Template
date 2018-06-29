import numpy as np
import cv2
from OpenPose.OpenPosePredict import *
from OpenPose.OpenPoseDraw import drawSkeleton
from util import *

def spin(processor, grayscale=False, write=False):
    cap = cv2.VideoCapture(0)
    i=0
    while(True):
        if i >= 100000:
            break
        # Capture frame-by-frame
        ret, frame = cap.read()
   	
        if grayscale: 
            # Our operations on the frame come here
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        # Process image
        frame = processor(frame)
    
        # Display the resulting frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
   
        if write: 
            # Write out to file
            cv2.imwrite("images/%06d.png" % i, frame)
    
        # Increment counter
        i+=1
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


def pipeline_print(frame):
    if frame is None:
        raise IOError("Frame was not read correctly")
    # Draw and display skeleton
    points = predictPoints(frame)
    img = drawSkeleton(points, frame)
    formed, angles = create_angles(points) 
    if formed:
        commands = anglesToCommands(angles)
        for com in commands:
            # ser.write(com.encode())
            print(com)
    else:
        print("No commands")
    return img

if __name__ == "__main__":
    spin(pipeline_print)