import matplotlib.pyplot as plt
import numpy as np
fobj=plt.figure(figsize=(7,7),facecolor='#FFFFFF')
spobj=fobj.add_subplot(1,1,1)
m_xticks='Jan Feb Mar Apr May Jun Jul Aug Sept Oct Nov Dec'.split()
l=np.arange(len(m_xticks))
barwidth=0.3
HighC=[32,32,33,33,32,30,30,30,30,30,31,31]
LowC=[23,23,24,25,25,24,24,24,24,24,23,23]
spobj.barh(l,HighC,height=barwidth,alpha=0.6,color='r',label='High C')
spobj.barh(l+barwidth,LowC,height=barwidth,alpha=0.6,color='b',label='Low C')
spobj.set_yticks(l+barwidth)
spobj.set_yticklabels(m_xticks)
spobj.set_ylabel('Months')
spobj.set_title('Temperature Chart')
spobj.legend(loc='upper right')
plt.show()
