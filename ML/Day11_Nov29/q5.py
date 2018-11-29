import cv2 as cv
import numpy as np
img=cv.imread("apple.jpg",0)
img=cv.bitwise_not(img)
cv.imshow('Result q5',img)
cv.imwrite('q5.jpg',img)
cv.waitKey(0)
