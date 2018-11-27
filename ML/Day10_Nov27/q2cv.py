import cv2 as cv
import numpy as np
img=np.zeros((512,512,3),np.uint8)
cv.line(img,(10,1),(500,100),(0,255,1),1)
cv.rectangle(img,(10,1),(500,100),(0,255,1),1)
cv.imshow("Image",img)
cv.waitKey(0)
