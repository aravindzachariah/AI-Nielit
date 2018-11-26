import numpy as np
s,e=input("Enter start and end number : ")
r,c=input("\nEnter the dimension : ")
x=np.zeros([r*c])
count=0
for i in range(s,e+1):
	x[count]=i
	count+=1
x=x.reshape(r,c)
print "\n",x
n=input("Enter a number: ")
y=x[x%n==0]
z=x[x%n!=0]
print "\nDivisible by",n,"\n",y
print "\nNot Divisible by ",n,"\n",z

