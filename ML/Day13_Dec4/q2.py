import cv2
import numpy as np
font=cv2.FONT_HERSHEY_SIMPLEX
img = cv2.imread('man.jpg',0)
kernel = np.ones((2,2),np.uint8)
img1 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.putText(img1,'MORPH_CLOSE',(45,50),font,1.5,(0,0,0),2)
img2 = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.putText(img2,'MORPH_OPEN',(45,50),font,1.5,(255,255,255),2)
cv2.putText(img,'Original Image',(45,50),font,1.5,(0,0,0),2)
imgc=np.hstack((img,img1,img2))
cv2.imshow('Result',imgc)
cv2.waitKey(0)
cv2.destroyAllWindows()
