import cv2 as cv
import numpy as np
img=np.zeros((512,512,3))
cv.ellipse(img,(255,255),(150,130),90,0,360,(0,255,255),-1)
cv.ellipse(img,(210,210),(50,30),90,0,360,(255,255,255),-1)
cv.ellipse(img,(295,210),(50,30),90,0,360,(255,255,255),-1)
cv.ellipse(img,(245,270),(100,80),30,0,100,(0,0,0),5)
#cv.ellipse(img,(245,270),(100,80),30,180,250,(0,0,0),5)
cv.imshow("Image",img)
cv.waitKey(0)
