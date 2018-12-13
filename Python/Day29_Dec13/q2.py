import matplotlib.pyplot as plt
import numpy as np
expl=[0.1,0,0,0]
fobj=plt.figure(figsize=(8,8),facecolor='#FFFFFF')
spobj=fobj.add_subplot(2,3,1)
party=[['INC','BJP','INDEPENDENT','OTHERS'],['INC','BJP','BSP+','OTHERS'],['TRS','INC','BJP','OTHERS'],['MNF','INC','BJP','OTHERS']]
state=['Madhya Pradesh','Rajasthan','Chattisgarh','Telengana','Mizoram']
seats=[[114,15,4,3],[99,73,3,14],[68,15,9,7],[88,19,1,11],[26,5,1,9]]
colrs=[['blue','orange','green','red'],['blue','orange','green','red'],['blue','orange','green','red'],['pink','blue','orange','green'],['violet','blue','orange','green']]
patches,texts=spobj.pie(seats[0],explode=expl,colors=colrs[0],shadow=True,startangle=45)
spobj.set_title(state[0])
spobj.legend(patches,party[0],loc='best')
spobj1=fobj.add_subplot(2,3,2)
patches,texts=spobj1.pie(seats[1],explode=expl,colors=colrs[1],shadow=True,startangle=45)
spobj1.set_title(state[1])
spobj1.legend(patches,party[0],loc='best')
spobj2=fobj.add_subplot(2,3,3)
patches,texts=spobj2.pie(seats[2],explode=expl,colors=colrs[2],shadow=True,startangle=45)
spobj2.set_title(state[2])
spobj2.legend(patches,party[1],loc='best')
spobj3=fobj.add_subplot(2,3,4)
patches,texts=spobj3.pie(seats[3],explode=expl,colors=colrs[3],shadow=True,startangle=45)
spobj3.set_title(state[3])
spobj3.legend(patches,party[2],loc='best')
spobj4=fobj.add_subplot(2,3,5)
patches,texts=spobj4.pie(seats[4],explode=expl,colors=colrs[4],shadow=True,startangle=45)
spobj4.set_title(state[4])
spobj4.legend(patches,party[3],loc='best')
plt.show()

