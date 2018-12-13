#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
fobj=plt.figure(figsize=(10,10),facecolor='#00FF00')
spobj=fobj.add_subplot(1,1,1)
stud_name_xticks='Ram Tom Raj Ravi Roy Anil'.split()
x_val=np.arange(len(stud_name_xticks))
#x_val=np.linspace(0,200,len(stud_name_xticks))
barwidth=0.3
stud_scores_m=[90,30,60,50,25,80]
stud_scores_s=[60,70,50,50,35,70]
spobj.bar(x_val,stud_scores_m,width=barwidth,alpha=0.5,color='b',label='maths')
spobj.bar(x_val+barwidth,stud_scores_s,width=barwidth,alpha=0.5,color='r',label='science')
#plt.xticks(x_val,stud_name_xticks)
spobj.set_xticks(x_val+barwidth)
spobj.set_xticklabels(stud_name_xticks)
spobj.set_xlabel('Candidates')
spobj.set_title('Assessment chart')
spobj.legend(loc='center')
plt.show()
