#!/usr/bin/python
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation as anm
fo=plt.figure(figsize=(6,6))
so=fo.add_subplot(111)
x=np.arange(5)
xlabels='apple orange mango grapes banana'.split()
sa=np.random.randint(1,90,5)
bc1=so.bar(x,sa,align='center')
so.set_xticks(x)
so.set_xticklabels(xlabels)
def animbar(i):
 global bc1
 sa=np.random.randint(1,90,5)
 print sa
 for bar1,h1 in zip(bc1,sa):
  bar1.set_height(h1)
 return bc1
anm1=anm.FuncAnimation(fo,animbar,interval=3000)
plt.show()
