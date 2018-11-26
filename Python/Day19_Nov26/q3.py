"""3.Write a python script(using numpy) to solve the following.

		A group of people took a trip on a bus at Rs.3.00 per child and Rs.3.20 per adult for 
 		a total of Rs.118.40
 		They took the train back at Rs.3.50 per child and Rs.3.60 per adult for 
		a total of Rs.135.20
		Print the number of children and adults.
		(hint : matrix multiplication and inverse to get the effect of division)
"""
  

import numpy as np
a=np.array([[3.0,3.2],[3.5,3.6]])
print "Induvidual Cost  Matrix(A) : \n",a
c=np.array([118.4,135.26])
print "\nTotal Cost Matrix(C) : \n",c
ai=np.linalg.inv(a)
xy=np.dot(ai,c)
print "\nNumber of Adults and Children : \n",np.rint(xy)  
