#!usr/bin/env python
def fact(n,f):
	if n!=1:
		f=f*n
		f=fact(n-1,f)
	return f
n1=input("Enter a number: ")
f1=fact(n1,1)
print "The factorial of ",n1," is ",f1
