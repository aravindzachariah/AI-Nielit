from textblob import TextBlob
s=raw_input("Enter the string :")
s1=TextBlob(s)
sc=s1.correct()
print sc
t=sc.translate(to='fr')
print t
