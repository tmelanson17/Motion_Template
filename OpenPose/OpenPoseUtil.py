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
    POSE_REF = { "ArmR": [5, 2, 3], "WristR": [2, 3, 4], "ArmL": [2, 5, 6], "WristL": [5,6,7]} 
  
