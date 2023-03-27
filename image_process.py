# https://www.pythonpool.com/opencv-solvepnp/
# https://amroamroamro.github.io/mexopencv/matlab/cv.initCameraMatrix2D.html
# https://stackoverflow.com/questions/70390470/problem-with-type-point3f-in-function-cv2-calibratecamera-python

import cv2
import numpy as np
import json

with open('points_2D.json', 'r') as f:
    data = json.load(f)

imgpoints = np.array(data, dtype = np.float32)

with open('points_m_3D.json', 'r') as f:
    data = json.load(f)

objpoints = np.array(data, dtype = np.float32)

img = cv2.imread("image.png")
size = img.shape[0:2]
dist_coeffs = np.zeros((4,1))

objpointslist = [objpoints]
imgpointslist = [imgpoints]

camera_matrix = cv2.initCameraMatrix2D(objpointslist,imgpointslist, size)
success, rotation_vector, translation_vector = cv2.solvePnP(objpoints, imgpoints, camera_matrix, dist_coeffs, flags=0)

# woo doesn't work