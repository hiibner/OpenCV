#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Huy Luong
# Created Date: 07.05.2019
# License: GNU GPL
# =============================================================================
# Imports
import cv2
import numpy as np
# =============================================================================

class SiftObject:
    def __init__(self, imgname, imgdata, keypoint, descriptor):
        """

        :param matching_result: An visualised image of the matching
        :param matches: List of the matched keypoints
        :param ratio: ratio of the keypoints of inputimage and compared image
        :param precision: Value of similarity to inputimage
        """
        self.imgname = imgname
        self.imgdata = imgdata
        self.img_data_skeleton = None
        self.keypoint = keypoint
        self.descriptor = descriptor
        self.keypoint_skeleton = None
        self.descriptor_skeleton = None
        self.precision = None
        self.matching_result = None
        self.matches = None
        self.ratio = None
        self.isencoded = False



    #encode the keypoints. Necessary to serialize the objects
    def encodeKeypointsToPickle(self):
        converted_keypoints = []
        converted_keypoints_skeleton = []
        for x in self.keypoint:
            temp = (x.pt, x.size, x.angle, x.response, x.octave,
                    x.class_id)
            converted_keypoints.append(temp)

        for x in self.keypoint_skeleton:
            temp = (x.pt, x.size, x.angle, x.response, x.octave,
                    x.class_id)
            converted_keypoints_skeleton.append(temp)


        self.keypoint = converted_keypoints
        self.keypoint_skeleton = converted_keypoints_skeleton

        self.isencoded = True

    #Decode the keypoints
    def decodePickleToKeypoints(self):
        decoded_keypoints = []
        decoded_keypoints_skeleton = []

        for x in self.keypoint:
            temp_feature = cv2.KeyPoint(x=x[0][0], y=x[0][1], _size=x[1], _angle=x[2],
                                        _response=x[3], _octave=x[4], _class_id=x[5])
            decoded_keypoints.append(temp_feature)

        for x in self.keypoint_skeleton:
            temp_feature = cv2.KeyPoint(x=x[0][0], y=x[0][1], _size=x[1], _angle=x[2],
                                        _response=x[3], _octave=x[4], _class_id=x[5])
            decoded_keypoints_skeleton.append(temp_feature)


        self.keypoint = decoded_keypoints
        self.keypoint_skeleton = decoded_keypoints_skeleton
        self.isencoded = False

