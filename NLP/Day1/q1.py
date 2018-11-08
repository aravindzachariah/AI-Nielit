import nltk
from textblob import TextBlob
p=TextBlob("My name is Aravind. India is my country. I drive Hyundai car")
s=p.sentences
w=p.words
n=p.noun_phrases
k=1
for i in s:
	print "Sentence %d : %s" % (k,i)
	k+=1
k=1
for i in w:
	print "Word %s : %s" % (k,i)
	k+=1
print "Nouns"
for i in n:
	print i.title()


