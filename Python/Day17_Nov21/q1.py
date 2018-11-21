#Q1 to Q3
import numpy as np
l1=[1,2,3,4,5]
a1=np.array(l1)
print a1
print "Array Type: ",a1.dtype 
print "Array Shape: ",a1.shape
print "Array Dimension: ",a1.ndim
print "Array Size: ",a1.size
print " ___________________________________"
#Q4
a2=np.arange(1,6)
print a2
print "Array Type: ",a2.dtype 
print "Array Shape: ",a2.shape
print "Array Dimension: ",a2.ndim
print "Array Size: ",a2.size
print " ___________________________________\n"

#Q5 and Q6
a3=np.ones([2,4,5])
print a3
print "Array Type: ",a3.dtype 
print "Array Shape: ",a3.shape
print "Array Dimension: ",a3.ndim
print "Array Size: ",a3.size
print " ___________________________________\n"

#Q7
a=np.array(l1)
a4=np.array(a)
a5=np.asarray(a)
print "array ",a," is ",a4," ",a is a4
print "asarray ",a," is ",a5," ",a is a5
print " ___________________________________\n"

#Q8 and Q9
i=input("Enter Identity matrix dimension: ")
ai=np.identity(i)
print ai
print "Array Type: ",ai.dtype 
print "Array Shape: ",ai.shape
print "Array Dimension: ",ai.ndim
print "Array Size: ",ai.size,"\n"
print " ___________________________________\n"

#Q9
a6=np.zeros_like(a3)
print a6
print "Array Type: ",a6.dtype 
print "Array Shape: ",a6.shape
print "Array Dimension: ",a6.ndim
print "Array Size: ",a6.size
print " ___________________________________\n"


