s=raw_input("Enter the sentence : ")
s=s.split()
k=0
for i in s:
	if i==i[::-1]:
		k+=1
print "There are ",k," palindromes"

