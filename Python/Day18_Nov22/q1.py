import numpy as np
a1=np.array([[1,2,3],[4,5,6]],dtype='i4')
print a1.shape
print a1.dtype
print a1,"\n"
a2=np.array(a1,dtype='f8')
print a2.shape
print a2.dtype
print a2,"\n"
a3=np.array(a2,dtype='i8')
print a3.shape
print a3.dtype
print a3,"\n"
a4=a1.astype(np.str)
print a4.shape
print a4.dtype
print a4,"\n"
a5=a3.astype(np.str)
print a5.shape
print a5.dtype
print a5,"\n"

#Question 6
a6=np.arange(1,13).reshape(4,3)
print a6,"\n"
print a6.shape,"\n"
print a6[0,:],"\n"
print a6[2,:],"\n"
print a6[:,1],"\n"
print a6[0:,:2],"\n"
print a6[:,2]

#Question 7
a7=np.arange(11,51).reshape(4,10)
a7[a7%5==0]=-1
print a7

#Question 8
print "\n"
def dig(ar):
	ar1=np.zeros(ar.shape)
	for i in range(0,ar.shape[1]):
        	ar1[i,i]=ar[i,i] 
	return ar1
a8=np.arange(1,10).reshape(3,3)
print a8,"\n"
print dig(a8),"\n"
