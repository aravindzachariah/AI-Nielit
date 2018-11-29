import cv2 as cv
import numpy as np
img=cv.imread("apple.jpg",0)
row,col=img.shape
M=cv.getRotationMatrix2D(((col-1)/2,(row-1)/2),45,1)
img1=cv.warpAffine(img,M,(col,row))
cv.imshow('Result q3',img1)
cv.imwrite('q3.jpg',img1)
cv.waitKey(0)
