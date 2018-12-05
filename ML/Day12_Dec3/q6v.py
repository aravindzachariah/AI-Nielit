import numpy as np
import cv2 
import sys
car_cascade=cv2.CascadeClassifier('cars.xml')
cap=cv2.VideoCapture('car1.avi')
wi=cap.get(3)
ht=cap.get(4)
if (cap.isOpened()==False):
	print "Error opening video"
count=0
while (cap.isOpened()):
	ret,frame=cap.read()
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cars=car_cascade.detectMultiScale(gray,1.12)
	cv2.line(frame,(0,int(ht/2)),(int(wi),int(ht/2)),(0,255,0),2)
	for (x,y,w,h) in cars:
		centx=(x*2+w)/2
		centy=(y*2+h)/2
		if centy<ht/2:
			cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
		else:
                	cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
	cv2.imshow('Detected',frame)
	cv2.waitKey(6)
