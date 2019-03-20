import cv2
import numpy as np



#matching_result ----> das img des matchings
#matches ----> die Keypoints die gematched wurden

class SiftObject:
    def __init__(self, imgname, imgdata, keypoint, descriptor):
        self.imgname = imgname
        self.imgdata = imgdata
        self.img_data_modified = None
        self.keypoint = keypoint
        self.descriptor = descriptor
        self.precision = None
        self.matching_result = None
        self.matches = None
        self.ratio = None

    def calculate_precision(self, matches, keypoints):
        self.precision = matches / keypoints



    def encodeKeypointsToPickle(self, keypoints):
        convertedKeyPoints = []
        for x in keypoints:
            temp = (x.pt, x.size, x.angle, x.response, x.octave,
                    x.class_id)
            convertedKeyPoints.append(temp)


        self.keypoint = convertedKeyPoints

    def decodePickleToKeypoints(self, encodedKeypoints):
        decodedKeyPoints = []

        for x in encodedKeypoints:
            temp_feature = cv2.KeyPoint(x=x[0][0], y=x[0][1], _size=x[1], _angle=x[2],
                                        _response=x[3], _octave=x[4], _class_id=x[5])
            decodedKeyPoints.append(temp_feature)

        self.keypoint = decodedKeyPoints

