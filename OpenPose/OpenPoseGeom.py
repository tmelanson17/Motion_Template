import numpy as np

def vector_angle(link1, link2):
	cosine = np.dot(link1, link2) / (np.linalg.norm(link1) * np.linalg.norm(link2))
	sine = np.cross(link1, link2) / (np.linalg.norm(link1) * np.linalg.norm(link2))
	angle = np.arctan2(sine, cosine)
	if angle < 0:
		angle += 2*np.pi 
	return angle 

if __name__ == "__main__":
	sqrt2 = np.sqrt(2)
	horz = np.array([1,0])
	second = np.array([[   1,       0],
		           [ sqrt2/2, sqrt2/2],
				   [       0,       1],
				   [-sqrt2/2, sqrt2/2],
				   [      -1,       0],
				   [-sqrt2/2,-sqrt2/2],
				   [       0,      -1],
				   [ sqrt2/2,-sqrt2/2]]
				  )

	print("Expected range:")
	for angle in np.arange(0, 2*np.pi, np.pi/4):
		print(np.mod(angle, 2*np.pi))
	print("Actual range:")
	for axis in second:
		print(vector_angle(horz, axis))