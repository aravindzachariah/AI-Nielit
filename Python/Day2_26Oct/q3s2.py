def fact(n,f):
	while n>0 :
		f=f*n
		n=n-1
	return f
n1=input("Enter the number : ")
f1=fact(n1,1)
print "The factorial of ",n1," is ",f1
