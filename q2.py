def ma(m,n):
	if(n>m):
		m=n
	return m
m=0
n1=input()
n2=input()
n3=input()
m=ma(m,n1)
m=ma(m,n2)
m=ma(m,n3)
print " The largest number is ",m
