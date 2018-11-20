import cv2
import os
from sift_object import sift_object
from matplotlib import pyplot as plt
import numpy as np
####https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_matcher/py_matcher.html


def chooselowervalue(x,y):
    if x > y:
        return y
    else:
        return x


def find_files(directory):
    global filenames
    for filname in os.walk(directory):
        filenames = filname[2]
        break
    return filenames

# img = cv2.drawKeypoints(img,keypoints,None)

# #ORB Detector
#orb = cv2.ORB_create()
#kp1, desc1 = orb.detectAndCompute(img1, None)
#kp2, desc2 = orb.detectAndCompute(img2, None)

#BruteForce SIFT
#Brute Force Matching ERKLAERBEDARF WIESO NORMHAMMING / CROSSCHECK nur das beste matching von der anderen descriptor menge
def start_matching(img1, img2, kp1, kp2, desc1, desc2, knn = True):
    if knn == True:
        bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=False)
        matches = bf.knnMatch(desc1, desc2, k=2)
        good_matches = []
        for m,n in matches:
            if m.distance < 0.75*n.distance:
                good_matches.append([m])

        matching_result = cv2.drawMatchesKnn(img1, kp1, img2, kp2,good_matches, None, flags=2)
        return matching_result, good_matches



    else:
        bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
        matches = bf.match(desc1, desc2)
        matches = sorted(matches, key=lambda x: x.distance)
        matching_result  = cv2.drawMatches(img1, kp1, img2, kp2, matches, None, flags=2)
        return matching_result, matches



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

def main():
    global databaseobjects
    databaseobjects = []
    directory = "C:/Users/Hyu/PycharmProjects/OpenCV/monograms"

    img1 = cv2.imread("byzturn.jpg", cv2.IMREAD_GRAYSCALE)
    sift = cv2.xfeatures2d.SIFT_create()
    kp1, desc1 = sift.detectAndCompute(img1, None)

    files = find_files(directory)

    for i in files:
        databaseimg = cv2.imread("monograms/" + str(i), cv2.IMREAD_GRAYSCALE)
        kp, desc = sift.detectAndCompute(databaseimg, None)
        monogram = sift_object(i, databaseimg, kp, desc)
        databaseobjects.append(monogram)

    for i in databaseobjects:
        matching_result, matches = start_matching(img1, i.imgdata, kp1, i.keypoint, desc1, i.descriptor, True)
        #numberofkeypoints = chooselowervalue(len(kp1),len(i.keypoint))
        #precision = len(matches)/numberofkeypoints
        precision = len(matches)/ len(i.keypoint)
        i.precision = precision
        i.matching_result = matching_result
        i.matches = matches


    databaseobjects = sorted(databaseobjects, key=lambda x: x.precision)

    print(databaseobjects[-1].precision)
    print(databaseobjects[-2].precision)
    print(databaseobjects[-3].precision)
    print(databaseobjects[-4].precision)

    # plt.imshow(end_result)
    # plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()




if __name__ == "__main__":
    main()
