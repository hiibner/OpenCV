import cv2
from skeletonizer import skeletonize
from tkinter import *
from tkinter import filedialog
from imgreader import start_matching
import numpy as np


root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
input1 = root.filename

global img2
img2 = cv2.imread(input1, cv2.IMREAD_GRAYSCALE)
print(img2)
# counterX = 0
# counterY = 0
# for x in img2:
#     counterY = 0
#     for y in x:
#         if y!=0:
#             img2[counterX][counterY]=255
#         counterY = counterY+1
#     counterX = counterX+1


# img2 = cv2.ximgproc.thinning(img2, thinningType=cv2.ximgproc.THINNING_ZHANGSUEN)
# img2 = cv2.bitwise_not(img2)
#
img2 = skeletonize(img2)



cv2.imshow("test", img2)
cv2.waitKey(0)

cv2.destroyAllWindows()


