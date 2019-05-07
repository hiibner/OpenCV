#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Huy Luong
# Created Date: 07.05.2019
# Inspired: http://opencvpython.blogspot.com/2012/05/skeletonization-using-opencv-python.html
# License: GNU GPL
# =============================================================================
# Imports
import cv2
import numpy as np
# =============================================================================

#Copyright© http://opencvpython.blogspot.com/2012/05/skeletonization-using-opencv-python.html

def skeletonize(img):
    #invert the inputimage
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



  #  FOR THICKER  LINES
  #   for i in range(2):
  #       skel = cv2.dilate(skel, element)
  ######################################

    #invert again to get a black image on white background
    skel = cv2.bitwise_not(skel)


    return skel