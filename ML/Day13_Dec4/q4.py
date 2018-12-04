import cv2 as cv
import numpy as np
img=cv.imread('building.png')
for i in range(2):
	img=cv.pyrDown(img)	
sobelx=cv.Sobel(img,cv.CV_8U,1,0,ksize=1)
sobely=cv.Sobel(img,cv.CV_8U,0,1,ksize=1)
imgc=np.hstack((img,sobelx,sobely))
cv.imshow('dst',imgc)
cv.waitKey(0)

