import cv2
from tkinter import filedialog
from tkinter import *

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
input1 = root.filename
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
input2 = root.filename

img1 = cv2.imread(input1, cv2.IMREAD_GRAYSCALE)

img2 = cv2.imread(input2, cv2.IMREAD_GRAYSCALE)

print(input1)
sift = cv2.xfeatures2d.SIFT_create()
kp1, desc1 = sift.detectAndCompute(img1, None)
kp2, desc2 = sift.detectAndCompute(img2, None)


bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=False)
matches = bf.knnMatch(desc1, desc2, k=2)
good_matches = []
for m, n in matches:
    if m.distance < 0.75*n.distance:
        good_matches.append([m])

matching_result = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good_matches, None, flags=2)

cv2.imshow("RESULT" ,matching_result)
cv2.waitKey(0)
cv2.destroyAllWindows()