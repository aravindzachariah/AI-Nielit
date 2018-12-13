#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
fobj=plt.figure(figsize=(6,4),facecolor='#00FF00')
spobj=fobj.add_subplot(1,1,1)
item_sales=[90,30,1,2,2,60,50,25,80,70,80,81,2,3,4,75,73,77,75,75,7,30,80,76,10]
item_sales1=[9,3,1,2,2,60,50,25,8,70,80,81,2,3,4,75,7,77,75,75,7,8,80,76,10]
num_bins=5
spobj.hist([item_sales,item_sales1],num_bins,stacked=True,histtype='barstacked')
item_sales.sort()		
print item_sales		
item_sales1.sort()		
print item_sales1		
plt.show()
