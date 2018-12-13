#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
fobj=plt.figure(figsize=(8,8),facecolor='#00FF00')
spobj=fobj.add_subplot(1,1,1)
stud_name_xticks='Ram Tom Raj Ravi Roy Anil'.split()
x_val=np.arange(len(stud_name_xticks))
score_mat=[80,90,95,85,5,90]
score_sci=[60,60,65,75,5,50]
score_lan=[40,90,45,35,5,25]
spobj.stackplot(x_val,[score_mat,score_sci,score_lan],labels=['maths','science','language'])
spobj.set_xticks(x_val)
spobj.set_xticklabels(stud_name_xticks)
spobj.margins(0.1)
spobj.legend(loc="best")
plt.show()
