from textblob import TextBlob
s=raw_input("Enter the sentence : ")
se=TextBlob(s)
print se.sentiment
