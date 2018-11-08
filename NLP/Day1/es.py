from textblob import TextBlob
while 1:
	s=raw_input("Enter the string :")
	s1=TextBlob(s)
	t=s1.translate(to='es')
	print t
