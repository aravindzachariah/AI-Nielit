import numpy as np
import cv2 
import sys
car_cascade=cv2.CascadeClassifier('cars.xml')
cap=cv2.VideoCapture('car1.avi')
if (cap.isOpened()==False):
	print "Error opening video"
while (cap.isOpened()):
	ret,frame=cap.read()
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cars=car_cascade.detectMultiScale(gray,1.12)
	for (x,y,w,h) in cars:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
	cv2.imshow('Detected',frame)
	cv2.waitKey(0)
