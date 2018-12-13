#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
fobj=plt.figure(figsize=(8,8),facecolor='#00FF00')
spobj=fobj.add_subplot(1,1,1)
item_sales_mu=[90,30,60,50,25,80,70,75,73,77,75,30,80,76,10]
item_sales_ch=[9,30,6,50,2,80,70,75,7,7,7,30,80,8,10]
item_sales_de=[19,30,16,50,12,80,70,75,17,17,17,30,80,18,10]
item_sales=[item_sales_mu,item_sales_ch,item_sales_de]
spobj.boxplot(item_sales,vert=True,showmeans=True)
spobj.set_yticklabels('Mumbai Chennai Delhi'.split())
spobj.margins(.02)
spobj.set_title('Metro Sales Analysis')
plt.show()
