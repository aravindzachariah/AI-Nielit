from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
s1="The mountains are beautiful"
s2="The mountains are everlasting tales of geography"
s3="The most beautiful time of the day is sunrise"
s4="Norway is well known for its costal mountains"
s5="you cant catch a the sunrise most of the year in Norway"
Q="Norway is a beautiful place"
doc=[s1,s2,s3,s4,s5]
tfid=TfidfVectorizer()
tfid.fit(doc)
dict=tfid.vocabulary_
print dict
for key in dict.keys():
	print key," ",dict[key]
doc1=[s1,s2,s3,s4,s5,Q]
m1=tfid.fit_transform(doc1)
cs=cosine_similarity(m1)
print "\n",cs
