import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from imgreader import start_matching
from imgreader import invertiere




img1 = cv.imread('image.png',0)                # trainImage
img2 = cv.imread('Byz_Mon_60.jpg',0)
# Initiate ORB detector
sift = cv.xfeatures2d.SIFT_create()
# find the keypoints and descriptors with ORB
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

matching_result, matches = start_matching(img1,img2,kp1,kp2,des1,des2,True)
plt.imshow(matching_result)
plt.show()
print(len(kp1))
print(len(kp2))
print(len(matches))

