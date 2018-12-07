from textblob import TextBlob
s=raw_input("Enter the sentence : ")
se=TextBlob(s)
pol=se.sentiment.polarity
sub=se.sentiment.subjectivity
if sub==0.0:
	print " It is a fact "
if pol>0:
	print " Positive "
elif pol==0:
	print " Neutral "
else:
	print " Negetive "
