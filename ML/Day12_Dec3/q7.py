import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('face.jpg',0)
edges = cv2.Canny(img,0,200)
edges2 = cv2.Canny(img,100,200)
pic=np.hstack((img,edges,edges2))
cv2.imshow('dst',pic)
cv2.waitKey(0)
