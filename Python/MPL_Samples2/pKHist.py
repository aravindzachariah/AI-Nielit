#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
fobj=plt.figure(figsize=(6,4),facecolor='#00FF00')
spobj=fobj.add_subplot(1,1,1)
item_sales=[90,30,1,2,2,60,50,25,80,70,80,81,2,3,4,75,73,77,75,75,7,30,80,76,10]
num_bins=5
spobj.hist(item_sales,num_bins)
plt.show()
