from pandas import DataFrame as f
import numpy as np
import random
item=['Onion','Sugar','Potato','Carrot']*5
place=['Delhi']*4+['Bhopal']*4+['Bangalore']*4+['Kolkata']*4+['Mumbai']*4
total=random.sample(range(10,50),20)
df=f({'Item':item,'Place':place,'Total':total})
print df,"\n\n"
while True:
	x=input("\n1.Display Itemwise Rank \n2.Display Itemwise Rank \n3.Exit\n>")
	if x==1:
		it=raw_input("Enter the item Name : ")
		il=df[df['Item']==it]
		il=il.copy()
		tol=il['Total']
		rank=tol.rank(ascending=False)
		il['Rank']=rank
		print il
	elif x==2:
		p=raw_input("Enter the place Name : ")
		pl=df[df['Place']==p]
                pl=pl.copy()
                tol=pl['Total']
                rank=tol.rank(ascending=False)
                pl['Rank']=rank
                print pl
	else:
		break
