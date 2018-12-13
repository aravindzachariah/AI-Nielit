#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
fobj=plt.figure(figsize=(6,6),facecolor='#00FF00')
spobj=fobj.add_subplot(1,1,1)
fruits='Apple Orange Grapes Mango Pineapple'.split()
sales=[30,40,25,10,35]
colrs='r y c g b'.split()
spobj.pie(sales,colors=colrs)
#spobj.pie(sales)
plt.show()
