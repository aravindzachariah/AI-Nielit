from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
Q="A revolution without dancing is a revolution not worth having."
f=open("V","r")
doc=[]
for s in f:
	doc.append(s.rstrip())
print doc
tfid=TfidfVectorizer()
tfid.fit(doc)
dict=tfid.vocabulary_
print dict
for key in dict.keys():
	print key," ",dict[key]
doc.append(Q)
m1=tfid.fit_transform(doc)
cs=cosine_similarity(m1)
print "\n",cs
