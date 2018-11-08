from textblob import TextBlob
N=open(raw_input("Enter the filename :"))
T=TextBlob(N.read())
w=T.words
s=T.sentences
print "\n \n The sentence is : \n----------------------"
for s1 in s:
	print s1 
print "----------------------\n--------Summary-------"
print "The no of sentences : ",len(s) 
print "The no of words     : ",len(w)
print "Important words     : "
for i,t in T.tags:
	if t=="NNS" or t=="NN":
		print "\t",i.title()
print "Title               :",s[0] 
