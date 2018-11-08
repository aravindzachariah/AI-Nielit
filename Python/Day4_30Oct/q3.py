def lcount(s1):
	d1=dict()
	for c in s1:
		if c in d1:
			d1[c]+=1
		else:
			d1[c]=1
	return d1
s=raw_input("Enter the sentence: ")
s2=lcount(s)
print s2
