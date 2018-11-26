import numpy as np
a=np.array([[3.0,3.2],[3.5,3.6]])
print "Induvidual Cost  Matrix(A) : \n",a
c=np.array([118.4,135.26])
print "\nTotal Cost Matrix(C) : \n",c
ai=np.linalg.inv(a)
xy=np.dot(ai,c)
print "\nNumber of adults,children :\n",np.rint(xy)  
