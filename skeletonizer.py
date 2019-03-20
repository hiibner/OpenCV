import cv2
import numpy as np


def skeletonize(img):
    img = cv2.bitwise_not(img)

    size = np.size(img)
    skel = np.zeros(img.shape, np.uint8)

    ret, img = cv2.threshold(img, 127, 255, 0)
    element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))

    done = False

    while (not done):

        eroded = cv2.erode(img, element)
        temp = cv2.dilate(eroded, element)
        temp = cv2.subtract(img, temp)
        skel = cv2.bitwise_or(skel, temp)
        img = eroded.copy()

        zeros = size - cv2.countNonZero(img)
        if zeros == size:
            done = True



    # FOR THICKER  LINES
    # for i in range(3):
    #     skel = cv2.dilate(skel, element)
    ######################################

    skel = cv2.bitwise_not(skel)


    return skel