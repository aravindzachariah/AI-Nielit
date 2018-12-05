import cv2
import numpy as np
font=cv2.FONT_HERSHEY_SIMPLEX
img = cv2.imread('man.jpg',0)
kernel1 = np.ones((2,2),np.uint8)
kernel2 = np.ones((2,2),np.uint8)
er= cv2.erode(img,kernel1,iterations=1)
dlt = cv2.dilate(er,kernel2,iterations=1)
cv2.putText(dlt,'Erode & Dialate',(45,50),font,1.2,(255,255,255),2)
cv2.putText(img,'Original Image',(45,50),font,1.5,(0,0,0),2)
imgc=np.hstack((img,dlt))
cv2.imshow('Result',imgc)
cv2.waitKey(0)
