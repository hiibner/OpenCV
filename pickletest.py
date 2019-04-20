import pickle
import cv2
from sift_object import SiftObject

img1 = cv2.imread("Abd_Mon_001.png", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("Abd_Mon_002.png", cv2.IMREAD_GRAYSCALE)
sift = cv2.xfeatures2d.SIFT_create()
kp1, desc1 = sift.detectAndCompute(img1, None)
kp2, desc2 = sift.detectAndCompute(img2, None)
n1 = SiftObject("Abd_Mon_001.png", img1, kp1, desc1)
n2 = SiftObject("Abd_Mon_002.png", img2, kp2, desc2)

# n1.encodeKeypointsToPickle()
# n2.encodeKeypointsToPickle()
list = []
list.append(n1)
list.append(n2)
for x in list:
    x.encodeKeypointsToPickle()


pickle_out = open("dict.pickle", "wb")
pickle.dump(list, pickle_out)

pickle_out.close()


pickle_in = open("dict.pickle", "rb")
listloaded = pickle.load(pickle_in)
print(listloaded)


# n2loaded.decodePickleToKeypoints()

# test1 = n1.keypoint[2]
# test2 = n2loaded.keypoint[2]
#
# print(test1.pt, test1.size, test1.angle, test1.response, test1.octave,
#                 test1.class_id)
# print(test2.pt, test2.size, test2.angle, test2.response, test2.octave,
#                 test2.class_id)
#
# print(test1 == test2)
#




