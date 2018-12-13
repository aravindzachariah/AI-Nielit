#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
fobj=plt.figure(figsize=(8,8),facecolor='#00FF00')
spobj=fobj.add_subplot(1,1,1)
fruits='Apple Orange Grapes Mango Pineapple'.split()
sales=[30,40,25,10,35]
colrs='r y c g b'.split()
#patches,texts=spobj.pie(sales,colors=colrs,shadow=True)
#patches,texts=spobj.pie(sales,colors=colrs,shadow=True)
patches,texts=spobj.pie(sales,colors=colrs,shadow=True,startangle=45)
print patches
print texts
plt.legend(patches,fruits,loc='best')
plt.show()
