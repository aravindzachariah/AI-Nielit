from textblob import TextBlob,Word 
import math
d1="The game of life is a game of everlasting learning" 
d2="The unexamined life is not worth living"
d3="Never stop learning"
s1=TextBlob(d1)
s2=TextBlob(d2)
s3=TextBlob(d3)
doclist=[s1,s2,s3]
wc=[]
for i in doclist:
	for j in i.words:
		a=i.words.count(j)
		wc.append((j,a))
for k in wc:
 print k
dn=len(doclist)
wi=raw_input(" Enter the word : ")
wi=Word(wi)
k=0
for i in doclist:
	if wi in i.words:
		k+=1
print (1+math.log((float)(dn)/(float)(k)))
