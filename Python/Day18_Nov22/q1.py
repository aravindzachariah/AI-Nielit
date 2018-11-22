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


