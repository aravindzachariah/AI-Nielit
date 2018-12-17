#!/usr/bin/python
import numpy as np
from matplotlib import pyplot as plt
import time
fo=plt.figure(figsize=(6,6))
so=fo.add_subplot(111)
while True:
 sa=np.random.randint(1,90,5)
 print sa
 so.cla()
 so.plot(sa)
 plt.pause(5)
 #plt.show()
 #time.sleep(5)
