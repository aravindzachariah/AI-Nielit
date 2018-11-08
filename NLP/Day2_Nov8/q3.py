from textblob import TextBlob
N=raw_input("Enter the sentence :")
T=TextBlob(N)
for w in T.tags:
	print w
