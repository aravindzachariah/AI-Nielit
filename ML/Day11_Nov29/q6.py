import cv2 as cv
import numpy as np
import sys
img1=cv.imread(sys.argv[1],0)
img2=cv.imread(sys.argv[2],0)
r1,c1=img1.shape
r2,c2=img2.shape
img=img1-img2
b=img.sum()
c=img1.sum()
if b==0:
	print "Images are same"
else:
	print "Images are not same" 
print "\nPercentage difference : ",((float)(c)/(float)(b))*100
#cv.imshow("Image",img)
#cv.waitKey(0)
