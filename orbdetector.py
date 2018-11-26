import cv2
import os
from sift_object import sift_object
from matplotlib import pyplot as plt
import numpy as np
####https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_matcher/py_matcher.html

def invertiere(x):
    return 1/x if x > 1 else x

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

    img1 = cv2.imread("test.png", cv2.IMREAD_GRAYSCALE)
    orb = cv2.ORB_create()
    kp1, desc1 = orb.detectAndCompute(img1, None)

    files = find_files(directory)

    for i in files:
        databaseimg = cv2.imread("monograms/" + str(i), cv2.IMREAD_GRAYSCALE)
        kp, desc = orb.detectAndCompute(databaseimg, None)
        monogram = sift_object(i, databaseimg, kp, desc)
        databaseobjects.append(monogram)

    for i in databaseobjects:
        print(i.imgname)

        matching_result, matches = start_matching(img1, i.imgdata, kp1, i.keypoint, desc1, i.descriptor)
        ratio = len(kp1) / len(i.keypoint)
        ratio = invertiere(ratio)
        i.precision = (len(matches) / len(kp1)) * ratio
        i.ratio = ratio
        i.matching_result = matching_result
        i.matches = matches


    databaseobjects = sorted(databaseobjects, key=lambda x: x.precision)

    result1 = databaseobjects[-1].matching_result
    result2 = databaseobjects[-2].matching_result
    result3 = databaseobjects[-3].matching_result
    result4 = databaseobjects[-4].matching_result
    result5 = databaseobjects[-5].matching_result

    plt.imshow(result1)
    plt.show()

    plt.imshow(result2)
    plt.show()

    plt.imshow(result3)
    plt.show()

    plt.imshow(result4)
    plt.show()

    plt.imshow(result5)
    plt.show()


if __name__ == "__main__":
    main()
