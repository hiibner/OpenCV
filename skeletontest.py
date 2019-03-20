import cv2
from skeletonizer import skeletonize
from tkinter import *
from tkinter import filedialog
from imgreader import start_matching



root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
input1 = root.filename

img1 = cv2.imread("monograms/Adra_02.png", cv2.IMREAD_GRAYSCALE)
img1 = skeletonize(img1)

img2 = cv2.imread(input1, cv2.IMREAD_GRAYSCALE)
img2 = skeletonize(img2)

sift = cv2.xfeatures2d.SIFT_create()
kp1, desc1 = sift.detectAndCompute(img1, None)
kp2, desc2 = sift.detectAndCompute(img2, None)
print(len(kp1))
print(len(kp2))
print(len(desc1))
print(len(desc2))
matching_result, matches = start_matching(img1, img2, kp1, kp2, desc1, desc2, True)
print(len(matches))

cv2.imshow("test", matching_result)
cv2.waitKey(0)
cv2.destroyAllWindows()


