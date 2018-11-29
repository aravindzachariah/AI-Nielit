import cv2 as cv
import numpy as np
img=cv.imread("apple.jpg",0)
img1=cv.resize(img,None,fx=2,fy=2,interpolation=cv.INTER_CUBIC)
cv.imshow('Result q2',img1)
cv.imwrite('q2.jpg',img1)
cv.waitKey(0)
