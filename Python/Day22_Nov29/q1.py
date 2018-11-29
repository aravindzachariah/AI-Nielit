import pandas as pd
from pandas import Series as s
from pandas import DataFrame as d
import numpy as np
d1={'Name':['Everest','K2','Kilimajaro'],'Height':[8,7.5,6.5]}
df1=d(d1)
print df1,"\n"

df1['rank']=0
print df1,"\n"

s1=s(list('abcd'))
print s1,"\n"
df2 = d(s1)
print df2,"\n"

a = np.array(range(15)).reshape((3,5))
df3= d(a,index="r1 r2 r3".split(),columns="c1 c2 c3 c4 c5".split())
print df3,"\n"

d2 = {'E_Name':{'E1':'Varun','E2':'Akshay','E3':'Tom'},'Eno':{'E1':104,'E2':105,'E3':106}}
df4=d(d2)
print df4,"\n"

Edesig=s(['Scientist','Officer','Engineer'],index="E1 E2 E3".split())
Edesig.name="desig"
print Edesig,"\n"
df4[Edesig.name]=Edesig
print df4,"\n"

s2=s(range(1,7))
s3=s([11,22,33,44,55,66])
s2.index=list('abcdef')
s3.index=list('defxyz')
is2=s2.index
is3=s3.index
is4=is2.union(is3)
print is4
s4=s2.reindex(is4,method="ffill")
print s4
