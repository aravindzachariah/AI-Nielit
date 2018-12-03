import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('sudoku.jpg',0)
img1 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow("Image after Adaptive Thresholding",img1)
cv2.waitKey(0)
