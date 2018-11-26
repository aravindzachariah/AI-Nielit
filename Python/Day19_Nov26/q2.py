import numpy as np
price=np.array([30000,35000,40000])
print "Price : ",price
sales=np.array([1,5,2,3,5,6,3,1,7,6,2,1]).reshape(3,4)
print "\nSales : \n",sales
s=np.dot(price,sales)
print "\nSales collection each day : ",s
