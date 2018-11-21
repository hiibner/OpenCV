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


#Brute Force Matching ERKLAERBEDARF WIESO NORMHAMMING / CROSSCHECK nur das beste matching von der anderen descriptor menge
def start_matching(img1, img2, kp1, kp2, desc1, desc2):
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(desc1, desc2)
    matches = sorted(matches, key=lambda x: x.distance)
    matching_result = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)
    return matching_result, matches

def main():
    global databaseobjects
    databaseobjects = []
    directory = "C:/Users/Hyu/PycharmProjects/OpenCV/monograms"

    img1 = cv2.imread("byzturn.jpg", cv2.IMREAD_GRAYSCALE)
    orb = cv2.ORB_create()
    kp1, desc1 = orb.detectAndCompute(img1, None)

    files = find_files(directory)

    for i in files:
        databaseimg = cv2.imread("monograms/" + str(i), cv2.IMREAD_GRAYSCALE)
        kp, desc = orb.detectAndCompute(databaseimg, None)
        monogram = sift_object(i, databaseimg, kp, desc)
        databaseobjects.append(monogram)

    for i in databaseobjects:
        matching_result, matches = start_matching(img1, i.imgdata, kp1, i.keypoint, desc1, i.descriptor)
        precision = 0 if len(i.keypoint) == 0 else len(matches)/ len(i.keypoint)
        i.precision = precision
        i.matching_result = matching_result
        i.matches = matches


    databaseobjects = sorted(databaseobjects, key=lambda x: x.precision)

    object = databaseobjects[-10]
    print(len(object.keypoint))
    testresult = cv2.drawKeypoints(object.imgdata, object.keypoint, None, flags=2)
    plt.imshow(testresult)
    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()




if __name__ == "__main__":
    main()
