""" 1. Write a python script to create and store a 2D array as a file by receiving 
	start and end numbers from user. The array should contain elements from 
	start to end incremented by 1. A suitable shape can be 
	decided by the programmer.0 can be used to fill columns if required.
	From this array, using conditional logic, create two new arrays , consisting of
	elements which are divisible by a given number,say dn1, in the first array
	and not divisible by dn1 in the second array.
"""
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

