import cv2 as cv
import numpy as np
img=cv.imread("apple.jpg",0)
row,col=img.shape
M=np.float32([[1,0,200],[0,1,100]])
img1=cv.warpAffine(img,M,(col,row))
cv.imshow('Result q1',img1)
cv.imwrite('q1.jpg',img1)
cv.waitKey(0)
