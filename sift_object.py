import cv2
import numpy as np

class sift_object:
    def __init__(self, imgname, imgdata, keypoint, descriptor):
        self.imgname = imgname
        self.imgdata = imgdata
        self.keypoint = keypoint
        self.descriptor = descriptor
        self.precision = None
        self.matching_result = None
        self.matches = None

    def calculate_precision(self, matches, keypoints):
        self.precision = matches / keypoints
