#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
fobj=plt.figure(figsize=(6,4),facecolor='#00FF00')
spobj=fobj.add_subplot(1,1,1)
stud_name_xticks='Ram Tom Raj Ravi Roy Anil'.split()
x_val=np.arange(len(stud_name_xticks))
#x_val=np.linspace(0,200,len(stud_name_xticks))
stud_scores=[90,30,60,50,25,80]
spobj.bar(x_val,stud_scores)
#plt.xticks(x_val,stud_name_xticks)
spobj.set_xticks(x_val)
spobj.set_xticklabels(stud_name_xticks)
print 
plt.show()
