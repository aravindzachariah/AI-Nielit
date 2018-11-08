def PoN(n):
	k=n-1
	while k>(n/2)-1:
		if n%k==0:
			print n," is not a prime number"
			return
		k-=1
	print n," is a prime number"
n1=input("Enter the number : ")
PoN(n1)
	
