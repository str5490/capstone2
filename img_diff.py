import numpy as np
import cv2

img1 = cv2.imread("img1.jpg")
img2 = cv2.imread("img2.jpg")
img1 = cv2.resize(img1, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
img2 = cv2.resize(img2, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
 
dst = cv2.absdiff(img1, img2)
dst = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
dst = cv2.GaussianBlur(dst, (21, 21), 0)
#dst = cv2.threshold(dst, 50, 255, cv2.THRESH_BINARY)[1]

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()