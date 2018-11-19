import cv2
import numpy as np

img1 = cv2.imread("Byz_Mon_60.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("byzturn.jpg", cv2.IMREAD_GRAYSCALE)
sift = cv2.xfeatures2d.SIFT_create()
kp1, desc1 = sift.detectAndCompute(img1, None)
kp2, desc2 = sift.detectAndCompute(img2, None)


# img = cv2.drawKeypoints(img,keypoints,None)

# #ORB Detector
#orb = cv2.ORB_create()
#kp1, desc1 = orb.detectAndCompute(img1, None)
#kp2, desc2 = orb.detectAndCompute(img2, None)




#fuer KNN crosscheck false ,bf.knnMatch, ratiotest auskommentieren , drawMatchesKnn ---> matches in good_matches
#Brute Force Matching ERKLAERBEDARF WIESO NORMHAMMING / CROSSCHECK nur das beste matching von der anderen descriptor menge
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck = True)
matches = bf.match(desc1,desc2)
#matches = sorted(matches, key = lambda  x:x.distance)
# good_matches = []
# for m,n in matches:
#     if m.distance < 0.75*n.distance:
#         good_matches.append([m])

matching_result  = cv2.drawMatches(img1, kp1, img2, kp2, matches, None, flags=2)



# fuer flann
# index_params = dict(algorithm = 0, trees = 5)
# search_params = dict()
# flann = cv2.FlannBasedMatcher(index_params, search_params)
# matches = flann.knnMatch(desc1,desc2,k=2)
# good_points = []
# for m, n in matches:
#     if m.distance < 0.6*n.distance:
#         good_points.append(m)

#result = cv2.drawMatches(img1,kp1 ,img2, kp2, matching_result[:10], None, flags=2)




cv2.imshow("Matching result", matching_result)
print(len(kp1))
print(len(kp2))
print(len(matches))
cv2.waitKey(0)
cv2.destroyAllWindows()