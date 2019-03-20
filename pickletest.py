import pickle
import cv2
from sift_object import *

img1 = cv2.imread("Adra_02.png", cv2.IMREAD_GRAYSCALE)

sift = cv2.xfeatures2d.SIFT_create()
kp1, desc1 = sift.detectAndCompute(img1, None)

n1 = SiftObject("Adra", img1, kp1, desc1)
# n2 = sift_object("Adra", img1, encodeKeypointsToPickle(kp1), desc1)
#
# pickle_out = open("dict.pickle", "wb")
# pickle.dump(n2, pickle_out)
#
# pickle_out.close()


pickle_in = open("dict.pickle", "rb")
n2loaded = pickle.load(pickle_in)

n2loaded.keypoint = decodePickleToKeypoints(n2loaded.keypoint)

test1 = n1.keypoint[0]
test2 = n2loaded.keypoint[0]

print(test1.pt, test1.size, test1.angle, test1.response, test1.octave,
                test1.class_id)
print(test2.pt, test2.size, test2.angle, test2.response, test2.octave,
                test2.class_id)

print(test1 == test2)





