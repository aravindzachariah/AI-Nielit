import cv2 as cv
import numpy as np
img1=cv.imread("apple.jpg")
img2=cv.imread("orange.jpg")
r1,c1,k1=img1.shape
r2,c2,k1=img2.shape
img1[:,c1/2:,:]=img2[:,c2/2:,:]
cv.imshow('Result q4',img1)
cv.imwrite('q4.jpg',img1)
cv.waitKey(0)
