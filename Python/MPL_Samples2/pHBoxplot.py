#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
fobj=plt.figure(figsize=(8,8),facecolor='#00FF00')
spobj=fobj.add_subplot(1,1,1)
item_sales_1=[90,30,60,50,25,80,70,75,73,77,75,30,80,76,10]
item_sales_2=[9,30,6,50,2,80,70,75,7,7,7,30,80,8,10]
item_sales=[item_sales_1,item_sales_2]
spobj.boxplot(item_sales,showfliers=False)
spobj.margins(.02)
plt.show()
