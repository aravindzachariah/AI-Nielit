#Q1 to Q3
import numpy as np
l1=[1,2,3,4,5]
a1=np.array(l1)
print a1
print a1.dtype 

#Q4
a2=np.arange(1,6)
print a2
print a2.dtype

#Q5 and Q6
a3=np.ones([4,10,10])
print a3
print a3.size

#Q7
a=np.array(l1)
a4=np.array(a)
a5=np.asarray(a)
print "array ",l1," is ",a4," ",a is a4
print "asarray ",l1," is ",a5," ",a is a5

