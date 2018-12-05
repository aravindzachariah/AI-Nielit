import pandas as pd
import numpy as np
from pandas import DataFrame as f
from pandas import Series as s

#Question 1  Create a (4,4)2D array  consisting of integers. 
a=np.array(range(1,17)).reshape(4,4)

#Question 2  Create a masked array from the above array by making numbers which are divisible by 3 as invalid values.
mska=np.ma.masked_array(a,mask=a%3 == 0)
print mska.mask,"\n"

#Question 3  Create a dataframe from the above masked array.
dfma =f(mska) 
print dfma,"\n"

#Question 4  Create a series of your own choice and do reindexing by exploring ffill,bfill,nearest etc
s1 = s(range(4),index=list("abcd"))
print s1,"\n"
print s1.reindex(list("abcde")),"\n"
print s1.reindex(list("abcde"),method="ffill"),"\n"
print s1.reindex(list("abcde"),method="bfill"),"\n"
#print s1.reindex(list("abecd"),method="nearest"),"\n"

#Question 5  Create a Dataframe object of your own choice and do reindexing.
ad=np.arange(1,10).reshape(3,3)
df1=f(ad,columns=list("abc"),index=list("xyz"))
print df1,"\n"
print df1.reindex(list("yzx")),"\n"

#Question 6  Create a dataframe object from the above array by making c1,c2,c3,c4 as column indices and r1,r2,r3,r4 as row indices.
a1=np.array(range(1,17)).reshape(4,4)
df2=f(a1,index="r1 r2 r3 r4".split(),columns="c1 c2 c3 c4".split() )

#Question 7.1 Using integer based indexing print the very first element(row 0, column 0) as a scalar,as a series,and as a dataframe.
print df2.iloc[0,0],"\n"

#Question 7.2 do 7.1 using label based indexing
print df2.loc['r1','c1'],"\n"

#Question 7.3 Print last two rows and columns
print df2.iloc[2:,2:],"\n"

#Question 8 Create another (4,4)2D array  consisting of integers, with c1,c2,c5,c6 as column indices and r3,r4,r5,r6 as row indices
a2=np.array(range(10,26)).reshape(4,4)
df3 = f(a2,index='r3 r4 r5 r6'.split(), columns='c1 c2 c5 c6'.split())

#	Create a dataframe from this array and do the following,
#		8a) add the two dataframes(QNo.7) using '+' operator,withoou any NaN in the result
#		8b) add the two dataframes using 'add' method,withoou any NaN in the result
print (df2+df3).fillna(0)
print df2.add(df3).fillna(0)

#Question 9   Create DataFrame obj(shape 3,4) and from that create two Series objs(one for axis 0,other for axis 1)
#		perform subtraction operation for both cases(along the two axes)

