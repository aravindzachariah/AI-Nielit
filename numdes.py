n1=input("Enter the number of times: ")
def l(n):
	if n>=1 :
		print n
		n=n-1
		l(n)
l(n1)
